import sys
import os

sys.path.append("..")

from util.TranscriptReader import TranscriptReader
from datasets.Preprocessor import Preprocessor

data_path = os.getcwd().replace("app", "data/")

if __name__ == '__main__':
    # read transcripts and load in dataframe
    transcript_reader = TranscriptReader()
    all_participants = transcript_reader.transcripts_to_dataframe(data_path)

    windows_size = 30
    preprocessor = Preprocessor(data_path)
    phrases_lp = preprocessor.prepare_dataset_to_model(all_participants)

    phrases_lp.to_csv(data_path + 'phrases_lp.csv', sep='\t')
    print("File was created")

