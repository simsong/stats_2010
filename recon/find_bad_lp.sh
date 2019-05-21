for i in  /workdir/slgarfinkel/2010_recon/ca/*/lp/*.lp.gz ; do echo -n === $i === ; zcat $i | tail -1 | grep -v End ; echo ; done
