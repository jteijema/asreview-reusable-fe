from pathlib import Path

from asreview.models.feature_extraction.base import BaseFeatureExtraction
import numpy as np
from sentence_transformers.SentenceTransformer import SentenceTransformer


class MiniLMReuse(BaseFeatureExtraction):
    """SBert feature extractor that reuses feature matrices."""

    name = "reuseable_MiniLM"

    def __init__(self,
                 *args,
                 model_name='all-MiniLM-L12-v2',
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.show_progress_bar = True
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name,
                                         device='cpu',
                                         )

    def transform(self, texts):
        cache_fp = Path("feature_matrix.npy")

        # load model if exists
        if cache_fp.exists():
            print('Loading matrix from: ' + str(cache_fp))
            return np.load(cache_fp)
        else:
            print('Calculating feature matrix')
            feature_matrix = self.model.encode(
                texts,
                show_progress_bar=self.show_progress_bar,
            )

            print('Saving matrix to: ' + str(cache_fp))
            np.save(cache_fp, feature_matrix)

            return feature_matrix
