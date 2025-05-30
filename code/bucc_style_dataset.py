import random

import utils as utils

random.seed(42)

def train_test_split(split_full_dataset):
    '''Split a full dataset into a training and test dataset.'''
    len_dataset = len(split_full_dataset)
    split_len = len_dataset // 4
    print(f'Dataset length: {len_dataset}.')
    train_set = [sent.strip() for sent in split_full_dataset[:split_len]]
    test_set = [sent.strip() for sent in split_full_dataset[split_len:]]
    print(len(train_set), len(test_set))
    return train_set, test_set #'\n'.join(train_set), '\n'.join(test_set)

def parallel_to_dictionary(source_sentence, target_sentence):
    '''Convert two lists of source and target parallel sentences into a dictionary.'''
    n = len(source_sentence)
    assert n == len(target_sentence), f'The two lists do not have the same length: {n}, {len(target_sentence)}.'
    parallel_dictionary = {source_sentence[i]: target_sentence[i] 
                           for i in range(n) if len(source_sentence[i]) > 2} 
    return parallel_dictionary

def filter_parallel(source_list, target_list):
    '''Filter parallel sentences to remove duplicated pairs.'''
    n = len(source_list)
    assert n == len(target_list), f'The two lists have different number of elements: {n} and {len(target_list)}.'
    sentence_pairs = [(source_list[i], target_list[i]) for i in range(n)]
    return utils.deduplicate_list(sentence_pairs) # set

def create_dataset(monolingual_source, monolingual_target, parallel_source_list, parallel_target_list, seed=42):
    '''Create two monolingual datasets with injected parallel sentences.'''
    split_mono_source = monolingual_source #utils.text_to_line(monolingual_source)
    split_mono_target = monolingual_target #utils.text_to_line(monolingual_target)
    print(f'{len(split_mono_source)} monolingual source sentences.\n{len(split_mono_target)} monolingual target sentences.')
    assert not ('' in split_mono_source and '' in split_mono_target), 'Empty line in monolingual corpus list'

    # Add parallel sentences
    filter_parallel_list = filter_parallel(parallel_source_list, parallel_target_list)
    filter_parallel_list = [sent_pair for sent_pair in filter_parallel_list 
                            if (len(sent_pair[0]) > 2) and (len(sent_pair[1]) > 2)]
    filter_para_source_list = [sent_pair[0] for sent_pair in filter_parallel_list]
    filter_para_target_list = [sent_pair[1] for sent_pair in filter_parallel_list]
    
    # Create parallel sentence dictionary
    parallel_dict = parallel_to_dictionary(filter_para_source_list, filter_para_target_list)
    split_mono_source.extend(filter_para_source_list)
    split_mono_target.extend(filter_para_target_list)
    
    # Remove potential duplicated sentences
    split_mono_source = list(set(split_mono_source))
    split_mono_target = list(set(split_mono_target))
    print(f'Whole corpus:\n{len(split_mono_source)} monolingual source sentences.\n{len(split_mono_target)} monolingual target sentences.')

    # Shuffle both monolingual texts
    random.seed(seed)
    random.shuffle(split_mono_source)
    random.shuffle(split_mono_target)
    assert not ('' in split_mono_source and '' in split_mono_target), 'Empty line in shuffled corpus list'
    # Creating dictionary with sentences and padded ID
    source_dict = {split_mono_source[i]: f'src-{i:07}' for i in range(len(split_mono_source))}
    target_dict = {split_mono_target[i]: f'trg-{i:07}' for i in range(len(split_mono_target))}
    gold_pair_list = [(source_dict[src_sent], target_dict[trg_sent]) for src_sent, trg_sent in parallel_dict.items()]

    # Final files: monolingual corpora and gold pair file
    final_source_list = [f'src-{i:07}\t{split_mono_source[i]}' for i in range(len(split_mono_source))]
    final_target_list = [f'trg-{i:07}\t{split_mono_target[i]}' for i in range(len(split_mono_target))]
    print(final_source_list[0], final_target_list[0])
    gold_list = [f'{pair[0]}\t{pair[1]}' for pair in gold_pair_list]

    return '\n'.join(final_source_list), '\n'.join(final_target_list), '\n'.join(gold_list)

def split_shuffle_create_corpus(mono_src, mono_trg, para_src, para_trg):
    '''Automatise train-test split, shuffling, and creation of BUCC-style corpus).
    
    Input is a split list.'''
    # Train-test split
    train_split_mono_src, test_split_mono_src = train_test_split(mono_src) 
    train_split_mono_trg, test_split_mono_trg = train_test_split(mono_trg)
    train_split_para_src, test_split_para_src = train_test_split(para_src) 
    train_split_para_trg, test_split_para_trg = train_test_split(para_trg)
    print('' in train_split_mono_src, '' in train_split_mono_trg, 
          '' in train_split_para_src, '' in train_split_para_trg)

    # # Create parallel sentence dictionary
    # train_parallel_dict = parallel_to_dictionary(train_split_para_src, train_split_para_trg)
    # test_parallel_dict = parallel_to_dictionary(test_split_para_src, test_split_para_trg)

    # Create the datasets
    train_mono_src, train_mono_trg, train_gold_par = create_dataset(
        train_split_mono_src, train_split_mono_trg, train_split_para_src, train_split_para_trg, seed=42)
    
    test_mono_src, test_mono_trg, test_gold_par = create_dataset(
        test_split_mono_src, test_split_mono_trg, test_split_para_src, test_split_para_trg, seed=42 + 1)

    return [[train_mono_src, train_mono_trg, train_gold_par], 
            [test_mono_src, test_mono_trg, test_gold_par]]

def save_files(src, trg, main_path, data_list):
    '''Save created BUCC-style files.
    
    data_list is the output of the split_shuffle_create_corpus function.'''
    with open(f'{main_path}/{src}-{trg}.train.{src}', 'w') as f:
        f.write(data_list[0][0])
    with open(f'{main_path}/{src}-{trg}.train.{trg}', 'w') as f: 
        f.write(data_list[0][1])
    with open(f'{main_path}/{src}-{trg}.train.gold', 'w') as f: 
        f.write(data_list[0][2])

    with open(f'{main_path}/{src}-{trg}.test.{src}', 'w') as f:
        f.write(data_list[1][0])
    with open(f'{main_path}/{src}-{trg}.test.{trg}', 'w') as f:
        f.write(data_list[1][1])
    with open(f'{main_path}/{src}-{trg}.test.gold', 'w') as f:
        f.write(data_list[1][2]) 