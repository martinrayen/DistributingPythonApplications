# Import the required modules.
import os
import re
import wx
import sys
import json
import numpy as np
import pandas as pd
import sklearn
from os import path
from datetime import datetime
from classMLModelingPipeline import *

def get_path(wildcard):
    try:
        app = wx.App(None)
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Choose a training file.', 
                           wildcard=wildcard, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            path = None
        dialog.Destroy()
        with open(r"ErrorLog.txt","w+") as f:
            f.write("Successful write.")
        return path
    except:
        with open(r"ErrorLog.txt","w+") as f:
            f.write(str(sys.exc_info()))


def instantiateMLPipleline():
    try:
        # Set the log variables.
        s_classApplication  = 'SampleApp'
        s_classMethod       = 'CreateAppDirectories'
        s_statusType        = 'Success'
        s_statusDescription = 'Successfull write operation.'
        # Call the funtion to get the input files.
        global s_infile
        s_infile = get_path('*.xlsx')
        s_infile = s_infile.replace("\\","\\\\")
    
        # Get the current working directory.
        s_path = os.getcwd()
        s_path = s_path.replace("\\","\\\\")
        s_basefile = os.path.basename(s_infile)
        global s_basefile_csv
        s_basefile_csv = (os.path.splitext(s_basefile)[0]) + '.csv'
    
        # Check, if path exists in system path,else add.
        if s_path in os.environ:
            sys.path.append(s_path)
    
        # Open and read the App Configuration using json.
        with open(s_path + '\\AppConfig.txt') as json_file:
            # Load the App config details.
            data = json.load(json_file)
            # For each entry in json, extract App config parameters.
            for p in data['AppConfig']:
                global applConfig
                applConfig = modMLModelingPipeline  (  p['Id'],
                                                        p['Name'],
                                                        p['Source'],
                                                        p['Output'],
                                                        p['TrainedModel'],
                                                        p['ExecutionLog'],
                                                        p['ExecutionLogFileName'],
                                                        p['FeedActiveSheet'],
                                                        p['FeedSkipRows'],
                                                        p['Archive']
                                                      )
        #===== Create Application Directories ============================================================
        applConfig.CreateAppDirectories()
        applConfig.WriteToActivityLog(s_classApplication,
                                      s_classMethod,
                                      s_statusType,
                                      s_statusDescription
                                     )
    except AttributeError:
        s_statusDescription = 'No file has been choosen!!!!'
        raise Exception(s_statusDescription)
    except:
        print("Unexpected error")
        s_statusDescription = 'Unexpected error : ' 
        s_statusDescription = s_statusDescription + str(sys.exc_info())
        raise Exception(s_statusDescription)
#===================================================================================================

if __name__ == "__main__":
    instantiateMLPipleline()
    input("Press enter to exit ;")