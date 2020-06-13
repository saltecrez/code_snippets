#!/bin/bash

# Description: automatically dump the databases  
# Author: Elisa Londero <elisa.londero@inaf.it>
# Date: June 2020


# ------------------- #
# START configuration #
# ------------------- #
dumps_folder=/home/controls/dumps/
db_user='root'
db_pwd='***REMOVED***'

dump_cmd="mysqldump -u${db_user} -p${db_pwd}"

dump_1="$dump_cmd datamodel_captures > datamodel_captures.sql"
dump_2="$dump_cmd datamodel_events > datamodel_events.sql"
dump_3="$dump_cmd metadata_prisma > metadata_prisma.sql"
dump_4="$dump_cmd prisma_archive_database > prisma_archive_database.sql"
dump_5="$dump_cmd prisma_calib > prisma_calib.sql"
dump_6="$dump_cmd prisma > prisma.sql"
# -----------------   #
# END configuration   #
# -----------------   #


tgz_ext=".tar.gz"
todays_folder=$(date +'%Y%m%d')
one_month_ago=$(date +'%Y%m%d' --date='-1 month')

cd $dumps_folder

if [ -d "$todays_folder" ]; then
	exit 1
else
	mkdir $todays_folder
	cd $todays_folder

        # ------------------- #
        # START configuration #
        # ------------------- #
	# start datamodels #
	eval $dump_1	
	eval $dump_2	
	# end datamodels   #

	# start metadata #
 	eval $dump_3	
 	eval $dump_4	
	# end metadata   #

	# start web databases #
 	eval $dump_5	
 	eval $dump_6	
	# end web databases   #
        # -----------------   #
        # END configuration   #
        # -----------------   #

	cd ../
	tar -czvf $todays_folder$tgz_ext $todays_folder
	rm -rf $todays_folder

	for entry in `ls`; do
		date="${entry%%.*}"
		if [ "$date" -le "$one_month_ago" ]; then
			rm -rf $date$tgz_ext
		fi
	done
fi
