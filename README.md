# A Dashboard Visualization App for the KSI (Kill or Serious Injured) Accidents related to Pedestrian in GTA/Toronto

## Prepared for Toronto Police Service (Open Data) by Tony Chan

<br />

## WARNING: This is a PRIVATE repository

THIS REPOSITORY IS ONLY INTENDED FOR PERSONAL USE OLNLY. AND, THE SOLE PURPOSE IS TO TRACK CODE CHANGES AND FOR DOCUMENTATION OF CODE  

## ALTHOUGH THIS REPO DO NOT INCLUDE ANY PERSONAL DATA, IT IS PROHIBITED TO OBTAIN AND USE ANY PERTAINING DATASET FOR OTHER USES

<br />

This readme.md file contains documentation for the steps to rebuild this app from GIT.  This repo contains codes to build a visualization dashboard using DASH/FLASK. This app allows you to visualize the dataset obtained from Open Data from Toronto Police Service (TPS), and enable deeper understanding behind the mechanism of collision accidents that are related to pedestrians within the GTA area.

## Prerequisites

To further develop this code, the following tools are needed.

- Visual Sutdio Code
- Anaconda
- Python Extension for VS Code

<br />

## To clone this repo on your machine

```sh
git config --global user.name “your_handle”
git config —-global user.email “your@email.com”
git clone https://github.com/todatech/tps-ksi-ped.git
```

<br />

## Setting the environment to develop this code

### Create Your Virtual Environment

```sh
python3 -m venv env
```

<br />

### Launch your virtual environment  

A. **In VSCode**  

Run Terminal: Create New Integrated Terminal (⌃⇧`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.  

or

B. **run in command line**

```sh
source env/bin/activate
```

### Install Packages (from a prepackaged list of programs)

```sh
pip install -r requirements.txt
```

<br />

## Running the Main Dash App

1. To run the Main App, run the following line.

    ```sh
    python index.py
    ```

    Open browser in your local machine and navigate http://localhost:8050/


<br />

gitlab: tps-ksi-ped

