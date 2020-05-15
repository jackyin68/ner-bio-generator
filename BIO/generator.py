# bio data generator for nre, KG

import codecs
import os
import pickle
import tensorflow as tf

from data_utils import load_word2vec, input_from_line
from model import Model
from utils import get_logger, create_model
from utils import load_config
from BIO.postprogress import correction_bio

flags = tf.app.flags
flags.DEFINE_string("raw_file", os.path.join("rawdata", "article.txt"), "Path for raw data")
flags.DEFINE_string("bio_file", os.path.join("rst", "article-bio.txt"), "Path for bio data")
flags.DEFINE_string("bio_cor_file", os.path.join("rst", "article-cor-bio.txt"), "Path for bio data")
flags.DEFINE_string("map_file", "../maps.pkl", "file for maps")
flags.DEFINE_string("ckpt_path", "../ckpt", "Path to save model")
flags.DEFINE_string("config_file", "../config/config_file", "File for config")
flags.DEFINE_string("log_file", "../log/generator.log", "File for log")
FLAGS = tf.app.flags.FLAGS


def load_article_sentences(path):
    sentences = []
    sentence = []
    for line in codecs.open(path, 'r', 'utf8'):
        line = line.strip()
        if not line:
            if len(sentence) > 0:
                sentences.append(sentence)
                sentence = []
        else:
            sentence.append(line)
    if len(sentence) > 0:
        sentences.append(sentence)
    return sentences


def save_to_file(bio_file, sentence, tags_result):
    for i, word in enumerate(sentence):
        word = word.strip()
        line = word + " " + tags_result[i] + "\n"
        bio_file.write(line)
    bio_file.write("\n")


def evaluate_sentences(sentences, bio_file):
    config = load_config(FLAGS.config_file)
    logger = get_logger(FLAGS.log_file)
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True

    with open(FLAGS.map_file, "rb") as f:
        char_to_id, id_to_char, tag_to_id, id_to_tag = pickle.load(f)

    with tf.Session(config=tf_config) as sess:
        model = create_model(sess, Model, FLAGS.ckpt_path, load_word2vec, config, id_to_char, logger, False)
        for sentence in sentences:
            tags_result = model.evaluate_sentence(sess, input_from_line(sentence, char_to_id), id_to_tag)
            print(tags_result)
            save_to_file(bio_file, sentence, tags_result)


def bio_generator(raw_file_path, bio_file_path):
    sentences = load_article_sentences(raw_file_path)
    bio_file = open(bio_file_path, "w")
    evaluate_sentences(sentences, bio_file)
    bio_file.close()


def main(_):
    raw_file_path = FLAGS.raw_file
    bio_file = FLAGS.bio_file
    bio_cor_file = FLAGS.bio_cor_file
    bio_generator(raw_file_path, bio_file)  # bio data generator
    correction_bio(bio_file, bio_cor_file)  # bio data correction


if __name__ == "__main__":
    tf.app.run(main)
