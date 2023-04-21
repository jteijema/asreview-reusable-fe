# Template for extending ASReview with new reusable feature extractors.

For a simulation project, we needed a reusable feature extractor. Code is based on code by @PeterLombaers. See [asreview-simulation-project](https://github.com/jteijema/asreview-simulation-project) for the project info.

## Usage
ASReview will look for a file names feature_matrix.npy in the folder is was launched from. If found, this file is used instead of generating a new one. If no matrix is found, one is generated and stored to the folder.

## License

MIT license
