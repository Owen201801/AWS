##### create a new virtual environment

* virtualenv function -- creates the env
* source function/bin/activate -- login within the virtualenv
* pip3 install package_name  -- install the packages
* ls function/lib/python3.6/site-packages/ --path where packages are installed
* mv function/lib/python3.6/site-packages/package /home/ubuntu/path --move packages
* cd lambda -- get into lambda folder
* zip -r lambda.zip . -- zip all files
* aws s3api put-object --bucket bucketname --key keyobject --body file.zip -- load file on s3


