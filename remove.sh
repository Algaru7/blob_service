echo "***remove"
	docker stop blob
	docker rm -f blob

	docker stop auth
	docker rm -f auth

	docker stop dir
	docker rm -f dir