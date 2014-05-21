mkdir twitter_corpus
function do_scrape {
  python scrape.py $1 > twitter_corpus/$1
}
