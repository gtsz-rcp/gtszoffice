gtsz_docker_status=$(docker ps --filter name=app_db_1 --format "{{.Names}}");
if [ $gtsz_docker_status != 'app_db_1' ]; then
	docker-compose up -d;
else
	echo 'app_db_1 is already run'
fi;
