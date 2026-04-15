# VoiceLaTeX
A project to automatically turn voice into LaTeX.

The advantage of this over a mere voice-to-text translator is that this project allows for the configuration of which voice lines translate to what LaTeX formulas. In addition, voice-to-text to a scripting language is not greatly explored. 

The current pipeline uses the Whisper backend, developed by OpenAI, to do automatic speech recognition (ASR), converting audio time series data into text. This backend is supplemented by a config file, which declares certain morphemes to
be parsed into LaTeX a specific way. The model writes the final output into a TeX file, which is then hopefully compilable LaTeX. Currently, we aim for the libraries to be specified by the user, but this may change as development progresses.
