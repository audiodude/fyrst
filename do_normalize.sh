mkdir twitter_normalized
for stream in $(ls -1 twitter_corpus); do
    python normalize.py twitter_corpus/$stream > twitter_normalized/$stream
done
