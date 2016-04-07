files=`ls testdata/Our_Team/ | grep raw`

for f in $files; do
    echo $f
    ./ask testdata/Our_Team/$f 15 > testdata/result/$f.log
done
