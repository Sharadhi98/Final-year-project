curl -X POST -u "apikey:HZvhBrtA4EGIxYnKJJv8GQOBPeNaJlTXkXPeIIKEVE7V" \
--header "Content-Type: audio/flac" \
--data-binary @/home/apoos_maximus/sharadhi/illiterate-blind/speeches/stt.flac \
"https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4defdcc5-8735-4626-8d6b-8188ceb5c809/v1/recognize"
