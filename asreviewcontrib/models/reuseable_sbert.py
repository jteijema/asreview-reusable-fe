import json
from pathlib import Path

from asreview.models.feature_extraction.base import BaseFeatureExtraction
import numpy as np
from sentence_transformers import SentenceTransformer


class SBertReuse(BaseFeatureExtraction):
    """SBert feature extractor that reuses feature matrices."""

    name = "sbert_reuse"

    # We use "" as default for cache_fp because asreview configparser acts up.
    def __init__(
        self,
        *args,
        model_name='all-MiniLM-L12-v2',
        cache_fp="",
        show_progress_bar=True,
        model_kwargs=None,
        device='cpu',
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        if model_kwargs is None:
            model_kwargs = {}

        print(cache_fp)
        if cache_fp:
            self.cache_fp = Path(cache_fp)
        else:
            self.cache_fp = None
        print(self.cache_fp)
        self.show_progress_bar = show_progress_bar
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name, device=device, 
                                         **model_kwargs)
        self._param = {
            'model_name': self.model_name,
            'model_kwargs': json.dumps(model_kwargs)
        }
        if self.cache_fp is not None:
            self._param['cache_fp'] = str(self.cache_fp)

    @property
    def param(self):
        return self._param

    def transform(self, texts):
        if self.cache_fp is not None and self.cache_fp.exists():
            print('Loading matrix from: ' + str(self.cache_fp))
            return np.load(self.cache_fp)
        else:
            print('Calculating feature matrix')
            feature_matrix = self.model.encode(
                texts,
                show_progress_bar=self.show_progress_bar
            )
            if self.cache_fp is not None:
                print('Saving matrix to: ' + str(self.cache_fp))
                np.save(self.cache_fp, feature_matrix)
            return feature_matrix