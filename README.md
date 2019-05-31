# newspaper-tool

it is a python script connect to postgresql database for answer a three analysis questions for articles which attract readers for newspaper. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
1-
you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
              marwa@DESKTOP-640PB0R MINGW64 ~ (master)
              $ cd Downloads
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads (master)
              $ cd fullstack-nanodegree-vm-master
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads/fullstack-nanodegree-vm-master (master)
              $ cd fullstack-nanodegree-vm-master
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads/fullstack-nanodegree-vm-master/fullstack-nanodegree-vm-master (master)
              $ ls
              CODEOWNERS  README.md  vagrant/
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads/fullstack-nanodegree-vm-master/fullstack-nanodegree-vm-master (master)
              $ cd vagrant
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads/fullstack-nanodegree-vm-master/fullstack-nanodegree-vm-master/vagrant (master)
              $ ls
              catalog/  forum/  tournament/  Vagrantfile
              marwa@DESKTOP-640PB0R MINGW64 ~/Downloads/fullstack-nanodegree-vm-master/fullstack-nanodegree-vm-master/vagrant (master)
              $ vagrant up
2-
Download folder project from  https://github.com/mareleceng/news-tool and then you will need to unzip this file after downloading it. 

3- Download folder the source of psql database source file to run into vagrant folder shared from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.To build the reporting tool, you'll need to load the site's data into your local database. To load the data, cd into the vagrant directory and use the command cd into folder of project then run psql -d news -f newsdata.sql.
Here's what this command does:
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.   

### Prerequisites
What things you need to install the software and how to install them:

1- VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

2-Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
### Installing

marwa@DESKTOP-640PB0R MINGW64 ~ (master)
$ cd fsnd-virtual-machine

marwa@DESKTOP-640PB0R MINGW64 ~/fsnd-virtual-machine (master)
$ cd vagrant

marwa@DESKTOP-640PB0R MINGW64 ~/fsnd-virtual-machine/vagrant (master)
$ vagrant up

marwa@DESKTOP-640PB0R MINGW64 ~/fsnd-virtual-machine/vagrant (master)
$ vagrant ssh
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-75-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

7 packages can be updated.
0 updates are security updates.


The shared directory is located at /vagrant
To access your shared files: cd /vagrant
Last login: Wed May 29 12:46:25 2019 from 10.0.2.2
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ cd newsdata
vagrant@vagrant:/vagrant/newsdata$ ls
newsdata.sql  newsdb.py  newsdb.pyc  newspaper.py  Readme.txt
vagrant@vagrant:/vagrant/newsdata$
vagrant@vagrant:/vagrant/newsdata$ psql -d news -f newsdata.sql
vagrant@vagrant:/vagrant/newsdata$ python newspaper.py
 * Serving Flask app "newspaper" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)



## Authors

* **marwa ahmed** - *electrical engineering* 


## License

This project is licensed under full stack developper training course in udacity 
