files=`ls testdata/Our_Team/ | grep raw`

for f in $files; do
    echo $f
    grep '?' testdata/result/$f.log > testdata/result/$f.question
    ./answer testdata/Our_Team/$f testdata/result/$f.question > testdata/result/$f.answer
done
