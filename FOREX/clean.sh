for file in *.csv
do
        #tr ' ' ';' <"$file" >
        sed -e 's/\s\+/;/g' -i $file
        # $file | tr ' ' ';' -i $file
        filename="${file##*/}"
        echo $filename
        pair1=${filename:10:3}
        pair2=${filename:13:3}
        echo $pair1 $pair2

        #sed -e 's/$/${pair}/' -i $file
        sed "s|$|;${pair1};${pair2}|" -i $file
        #sed 's/.\{9\}$//' -i $file
done

