# JIRA/Confluence Training Instance

The purpose of this project is to enable the use of a JIRA/Confluence Starter
licence to be used to run up a temporary training instance of both products
linked together with JIRA as the IDAM master and the ability to link to JIRA
tickets from Confluence enabled for up to 10 users (as permitted by the
terms of the [starter licence](https://www.atlassian.com/licensing/starter)).

The software is to be run as two Docker containers orchestrated using the
```docker-compose``` tool to coordinate them.

## Current State
The instances can currently be run up using a dump of the JIRA/Confluence
data directories if using the embedded database option.

## The Plan

The aim is to automatically provision instances using a web driver
such as Selenium.  At the moment this is proving difficult due to some of the
asynchronous JavaScript used on the web-based provisioning wizard and the
lack of a scripted end-to-end provisioning option provided by the tools.

## Instructions to generate a data dump

Create empty tarballs for each of the products
* data_jira.tar.gz
* data_confluence.tar.gz

Run up the image using build.sh and up.sh or ```docker-compose up``` and go
through the provisioning process on each of the tools (JIRA is on port
8080, Confluence on 8090).  You can link Confluence to JIRA using
the hostname jira.

Tar up and extract each relevant data directory
* JIRA
  * ./jira-shell.sh
  * cd /opt/atlassian/jira/data
  * tar czf /data_jira.tar.gz .
  * exit
  * docker cp <image-id>:/data_jira.tar.gz ./data_jira.tar.gz
* Confluence
  * ./confluence-shell.sh
  * cd /opt/atlassian/confluence/data
  * tar czf /data_confluence.tar.gz
  * exit
  * docker cp <image-id>:/data_confluence.tar.gz ./data_confluance.tar.gz

Shut down the docker containers.  Then build and re-run them.  They should now be running
with the provisioned data.
