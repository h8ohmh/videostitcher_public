#!/usr/bin/env python
# encoding: utf-8
# TODO: Cluster encoding
# TODO: Append started files
# TODO: Dbgprint
# TODO: VerbosePrint
# TODO: Mencoding in eigene Temp Datei und dann protokoll welche datei fertig
# TODO: ErrorFiles recording
# TODO: Umbenennen der Datei in Datum
# TODO: AVIfix
# TODO: Help
# TODO: UDHCPD Start, Auto connect und mount



#!/bin/bash
# ffmpeg -err_detect ignore_err  -psnr -start_at_zero -copyts -copy_unknown -copytb 1 -f concat -safe 0 -i \
# <(for f in $PWD/*.mp4; do echo "file '$f'"; done) \
# -c copy output.mp4


from __future__ import print_function
from __future__ import (absolute_import, division,
						print_function, unicode_literals)

use_scoop= False

#import subprocess
from operator import itemgetter
from itertools import groupby #TODO Check ob vorhanden
from pprint import pprint
from pymediainfo import MediaInfo	#TODO
from operator import itemgetter
from collections import defaultdict

if use_scoop == True:
	import scoop

import numpy
import pandas
import zlib
import pprint
import re
import string
import collections
import csv
import datetime
import getopt
import glob
import random
import inspect
import json
import unicodedata
import locale
import mmap
import multiprocessing
import os
import pydoc
import pathlib #python 3
import shutil
import signal
import subprocess
import sys
import threading
import time
import unicodedata
import getopt
import hashlib
from functools import partial

locale.setlocale(locale.LC_ALL, 'de_DE')

global amrgcmd_base
global date_start_sec
global do_json_parse
global do_process
global do_process_json
global jsonpath
global mencoder_X264OPTS
global mencoder_crf
global mencoder_fps
global mencoder_scale2
global merge_method
global object_self
global opt_debug
global path_batch_output
global path_default
global path_default_pattern
global path_dir_output
global path_json_file
global path_startdir #TODO
global total_files #TODO

global errfiles
global date_start
global do_json_parse
global mencoder_threads
global mencoder_crf
global mencoder_fps
global mencoder_scale2
global mencoder_addX264OPTS
global mencoder_cachesize
global mencoder_X264OPTS
global do_process_json
global merge_method
global opt_debug
global total_files

#@VARIABLEN
fname_start=""
path_dir_output="/ddisk/recovered_high"
#path_dir_output="/nas0030/media/USB_HDD_5/recovered_high"
#path_dir_output="/output"
path_batch_output="$HOME//mergecmds.sh"
#path_startdir= "/recovered2" #TODO Namen
path_startdir= "/disk/recovered2/"
path_json_file="$HOME/video_output/video_stitch.json"
default_path_pattern=path_startdir+"/*/*.m2ts"	#TODO: path_default_pattern
#default_path_pattern=path_startdir+"/n37/*.m2ts"	#TODO: path_default_pattern
#default_path_pattern=path_startdir+"/n39/*.m2ts"	#TODO: path_default_pattern
#default_path_pattern=path_startdir+"/n43/*.m2ts"	#TODO: path_default_pattern


#GLOBAL BREAK FLAG
do_process= True

date_start=""
do_json_parse= True	#TODO
do_process_json= True
merge_method=1
opt_debug=0
total_files=2000000

#GKro 1523577600
#wiebü 139xx

#!/bin/python
# concat_str_01='
# import os
# import sys
# import datetime
# import getopt
# import glob
# import random
# import locale
# import mmap
# import os
# import pydoc
# import shutil
# import signal
# import getopt
# import zlib
# import pprint
# import re
# import string

# the_files=[



# NEU -oac lavc -lavcopts acodec=aac:abitrate=128
#<mencoder options>
mencoder_threads=4 #TODO abhängig von multiprocessing.pool
mencoder_crf=26
mencoder_fps=25
mencoder_scale2='1360:768'
mencoder_addX264OPTS=""
mencoder_cachesize=8096*2
mencoder_sound_or_no=[ "-lavc", "-oac" ]
mencoder_X264OPTS='crf='+str(mencoder_crf)+':trellis=1:threads=' \
	+ str(mencoder_threads) \
	+ ':ratetol=inf:frameref=2:bframes=2:8x8dct:ssim:psnr' \
	+ str(mencoder_addX264OPTS)
#</mencoder options>

errfiles= \
[
]

amrgcmd_base=[
		"",
		'mencoder',
		'x264',
		'avidemux3_cli',
		'mkvmerge',
		'avimerge',
		'ffmpeg'
	]

if len(date_start) == 0:
	date_sec_start=0
else:
	nix=0 #TODO


object_self=[]
#=======================================================================

def locale_value(number):
	return ("{:,}".format(number))
#=======================================================================

#=======================================================================

def screen_clr():
	os.system('cls' if os.name == 'nt' else 'clear')
#=======================================================================

#TODO
#=======================================================================
def screen_upd():
	pass
#=======================================================================

def worker(mrgcmd):	#TODO
	#print('mencoder %.32768s\n' % mrgcmd)
	#print("mencoder")
	pprint(mrgcmd)
	result= 0
	opt_debug= 0
	if(opt_debug > 0):
		print("Worker")
		#pprint(mrgcmd)
		result=1
	else:
		tmrgcmd=mrgcmd[:]
		tmrgcmd.insert(0, '/usr/bin/mencoder')	#TODO

		#tmrgcmd.insert(0, '/usr/bin/mencoder')
		#tmrgcmd.insert(0, 'ffmpeg') #TODO
		result= subprocess.call(tmrgcmd)
	#mrgcmd#
	#for i in amrgcmd:
		#print to batch file
	return result
#=======================================================================
def start_processes():
	print("...Starting '%.8192s'" % multiprocessing.current_process().name)
#=======================================================================
def signalhandler(signum, frame):
	print('Received:', signum)
	if signum == 20:
		print("Terminate Videostitcher")
		sys.exit()
	return
#<NEU MENCODER>
#				'-lameopts', 'cbr:br=128',
#				'-oac', 'copy',
#				'-abitrate=', '128',
#
		#fehlgeschlagen
				#'-oac','lavc',
				#'-lavcopts','acodec=ac3',
				#'-lavcopts', 'acodec=ac3:abitrate=224:',
				#'-nosound',

			#[ '-ovc', 'copy', '-oac', 'copy', '-of', 'rawvideo', '-noskip', '-idx', '-msgcolor' ], \
			#[ '-ovc', 'copy', '-oac', 'copy',  '-noskip', '-msgcolor', '-of', 'lavf', '-lavfopts', 'format=avi' ], \
		# [ '-ovc', 'x264', \ #neuester mencoder versuch
# #		'-x264encopts', 'level_idc=12:bitrate=128:subq=7:partitions=all:8x8dct:me=esa:me_range=23:frameref=6:trellis=1:b_pyramid:weight_b:mixed_refs:threads=0:qcomp=0.6:keyint=250:min-keyint=25:direct=temporal',
		# #'-x264encopts', 'bitrate=1024', \
		# '-oac', 'copy', \
		# '-of', 'lavf', \
		# #'-ofps', '', \
		# '-lavfopts', 'format=mpegts']
		#[ '-ovc', 'copy', '-lavcopts', 'vcodec=mpeg2video', '-oac', 'copy', '-of', 'mpeg']
#</Mencoder>
#ffmpeg -i input.m2ts -c:v copy -c:a aac -strict experimental -b:a 128k output.mp4
#TODO: Automatic connect
#sshfs -o allow_other -o TCPKeepAlive=yes user@192.168.178.32:/ /nas0030
#mount /dev/sdb1 /adisk
#reset; python ./videostitcher.py 2>&1 | tee videost.log
#reset; python ./videostitcher.py | tee /adisk/recovered/heute.log
#mencoder -ovc x264 INPUT.avi -x264encopts level_idc=12:bitrate=128:bframes=16:subq=7:partitions=all:8x8dct:me=esa:me_range=23:frameref=6 :trellis=1:b_pyramid:weight_b:mixed_refs:threads=0:qcomp=0.6:keyint=250:min-keyint=25 :direct=temporal -vf scale=240:192 -oac lavc -lavcopts acodec=libfaac:abitrate=56 -srate 48000 -af channels=2 -of lavf -ofps 25 -lavfopts format=mp4 -o OUTPUT.mp4
#encoder alternativen
#ffmpeg -i "concat:00019.MTS|00020.MTS|00021.MTS|00022.MTS" output.mp4
#mencoder -really-quiet -ovc lavc -lavcopts vcodec=mjpeg -mf fps=${FPS} -vf scale=${videoX}:${videoY} -o $output_video_file_name video_*.avi
#mencoder -oac copy -ovc copy -o output_file.mp4 -mf fps=30 input_file1.mp4 input_file2.mp4
#rm /home/video_output/video_stitch.json ; reset; python ./videostitcher.py

# letzte lösung:
# <start>
# IFS=$(echo -en "\n\b")
# for i in *.m2ts; do
# ffmpeg -i "$i" -vcodec mpeg4 -b:v 15M -acodec libmp3lame -b:a 192k "/adisk/recovered/$(basename "$i").mp4" &
# ffmpeg '-i', 00000.MTS|00001.MTS|00002.MTS" -c copy output.mts]
# done
# mencoder -oac copy -ovc copy -o output.mp4 1.mp4 2.mp4
# <ende>
		# mencoder_base="mencoder -cache 8096 -demuxer lavf -sws 9 -fps $((FPS*2)) -vf yadif=1,mcdeint,softskip -ofps $FPS"
		# enc="$mencoder_base -ovc x264 -oac copy -vf scale=$scale_to -x264encopts crf=$CRF:trellis=1:threads=0:ratetol=inf:frameref=2:bframes=2:8x8dct:ssim:psnr:$X264OPTS"
		# echo "$enc -o $dpath $sfpath"
		# cmd="$enc -o $dpath $sfpath"

class videostitcher:
			#TODO mencoder dict
		#TODO mencoder dict
	""" Class doc """
	#method=merge_method
	a_track=""
	command_udhcpd='bash ./udhcpd_server_start.sh'
	command_mount_dest='mount /dev/sdb1 /ddisk'
	command_call_self='reset; python ./videostitcher.py'
	command_sshfs='sshfs -o allow_other user@192.168.178.32:/ /nas0030'
	current_entry=[]
	dump_type="json"
	file_batch=""
	file_counter= 0
	file_csv_output=""
	file_log_output=""
	file_output_list=""
	fname_output=""	#TODO
	files= []
	found_date=False
	imp_hhmmss_format="%H:%M:%S"
	imp_yyymmddhhmmss_format="%Y-%m-%d %H:%M:%S"
	imp_yyyymmdd_format="%Y-%m-%d"
	jobs = []
	jsonfiles= None
	max_files= total_files
	media_info= ""
	merge_method=0
	mrg_ext="-x264.avi"	#TODO
	num_merge_methods= 1 # TODO min und
	opt_resume_json= True
	cpath_file_output=''
	mencoder_X264OPTS= \
		'crf='+str(mencoder_crf)+':trellis=1:threads=' \
		+ str(mencoder_threads) \
		+ ':ratetol=inf:frameref=2:bframes=2:8x8dct:ssim:psnr' \
		+ str(mencoder_addX264OPTS)

	mencodercmdline= \
				'-cache' + str(mencoder_cachesize) + \
				'-demuxer' + 'lavf' + \
				'-sws' + '9' + \
				'-fps' + str(mencoder_fps*2) + \
				'-vf' + 'yadif=1,mcdeint,softskip' + \
				'-ofps' + str(mencoder_fps) + \
				'-oac' + 'lavc' + \
				'-lavcopts' + 'acodec=aac:abitrate=128' + \
				'-ovc' + 'x264' + \
				'-vf' + 'scale=' + str(mencoder_scale2) + \
				'-forceidx' + \
				'-x264encopts' + mencoder_X264OPTS
	mrgcmd_opt_all_file=\
		[ \
			[ ], \
			[ #mencoder TODO
				'-cache', str(mencoder_cachesize),
				'-demuxer', 'lavf',
				'-sws', '9',
				'-fps', str(mencoder_fps*2), #TODO
				'-vf', 'yadif=1,mcdeint,softskip',
				'-ofps', str(mencoder_fps),
				'-oac', 'lavc',
				'-lavcopts', 'acodec=aac:abitrate=128',
				#'-nosound', #TODO
				#'-oac', 'copy',
				#'-oac', 'lavc',
				#'-lavcopts', 'acodec=libmp3lame:abitrate=128:',
				'-ovc', 'x264',
				'-vf', 'scale=' + str(mencoder_scale2),
				'-forceidx',
				'-x264encopts', mencoder_X264OPTS,
			],
			[ '', ''	#x264 TODO
			],
			[ #AVIDEMUX_CLI, \
				'--nogui',
				'--output-format', 'MP4',
				#'--rebuild-index',
				'--force-smart',
				'--save-raw-audio',
			],
			[ # Mencoder, Grösste Dateien, jedoch nicht mit VLC abspielbar\
				'-ovc', 'copy', \
				'-oac', 'copy', \
				'-noskip', \
				'-msgcolor', \
				'-forceidx',
				'-lavfopts', 'format=mpegts'
			],
			[ '-ovc', 'copy', '-oac', 'copy', '-forceidx', '-of', 'AVI'],
			[ '-ovc', 'copy', '-oac', 'copy', '-forceidx', '-of', 'MP4'],
			[ '-ovc', 'lavc', '-oac', 'copy', '-of', 'lavf' ],
		]

	mrgcmd_opt_per_file=[
		[''],
		[''], # mencoder
		[''], # x264
		['--append'], # ffmpeg
		[""],
	]
	mrgcmd_output=[ \
		'',\
		'-o', #mencoder
		'', #x264
		'--save', #ffmpeg
		'--save' ]
	mrgcmds=[]
	name_dir_output="video_output"
	opt_batchfile=True
	opt_debug=0
	opt_overwrite=False
	opt_photorec=True
	opt_verbose= 1
	opt_pause= False
	opt_stop_before_encoding= False
	path_batch_file=""
	path_batch_output=""
	path_csv_output=''
	path_current_file=""
	path_cwd="./" #TODO
	path_dir_output=""
	path_json_file=""
	path_output_list=""
	path_start_dir=""
	pool= []
	pool_outputs=[]
	pool_size= 6
	path_json_file=""
	python_vers=0
	results= {}
	seconds_since_1970= 0
	sorted_files= {}
	sshfs_cmd="sshfs -o allow_other -o TCPKeepAlive=yes user@192.168.178.32:/ /nas0030"
	start_cmd="rm /home/video_output/video_stitch.json ; reset; python ./videostitcher.py"
	string_glob=""
	json_file_already_loaded= False

	#rm /home/video_output/video_stitch.json ; reset; python ./videostitcher.py
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def __init__ (self, path_dir_output="./"):	#TODO verbessern
		""" Class initialiser """
		#signal.signal(signal.SIGINT, signal_handler_sigint)
		#self.path_output= output_path
		self.python_version= sys.version_info.major
		self.seconds_since_1970= datetime.datetime(1970, 1, 1)
		self.jsonfiles= pandas.DataFrame()
		self.path_dir_output= \
			os.path.realpath("%.8192s" % path_dir_output )
		if self.opt_verbose > 0:
			print('Output dir path: %.8192s' % self.path_dir_output)

		# Check whether output path exists
		if not os.path.exists(self.path_dir_output):
			try:
				os.makedirs(self.path_dir_output)
			except:
				print('ERROR: No output dir "%.8192s", EXIT'\
				% self.path_dir_output)
				sys.exit(-1)

	# def sort_entries(self):
		# files_by_date= sorted(files, key=itemgetter('date'))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	def open_batch_file(self):
		batchcmds=[]
		if self.opt_batchfile == True:
			print('...Resetting batch file')
			try:
				#TODO
				with open("./video_output/mergecmds.sh", 'w') as f:
					f.close()
			except:
				print('ERROR in reset batch file');
				sys.exit(-1)
		pass
#=======================================================================
	def save_files_to_json(self):
		print('... backup previous json file "%.8192s"' \
			% self.path_json_file)
		#self.backup_file(self.path_json_file)
		print('... writing json file "%.8192s"' \
			% self.path_json_file)
		try:
			self.jsonfiles.drop_duplicates(keep='first')
		except:
			pass
		try:
			self.jsonfiles.to_json(self.path_json_file)
		except:
			print('ERROR - Can not save Json file "%s"'
				% self.path_json_file )
		return

	#	with open(self.path_json_file,'w+') as f:

			# for jentry in self.jsonfiles: #TODO
				# self.files.append(jentry)
	#			% self.path_json_file)
			#pprint(self.files)
	#		print("len files %s" % len(self.files))
			#ew_l= [dict(t) for t in {tuple(sorted(entry.items())) for entry in self.jsonfiles}]
	#		json.dump(self.files, f)
			#f.write("\n")
	#		f.close()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
#	multiprocessing.net!!!
	def json_signalhandler(self, signum, frame):
		global do_process
		print('Received:', signum)
	#		raise SystemExit('Exiting') #TODO
		#if signum == signal.SIGINT: #CTRL-Z = 20
		print("Terminate Videostitcher")
		print("Please wait - no more keyboard touch!")
		do_process= False
		return
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def process_media_file(self):
		global MediaInfo
		#signal.signal(20, json_signalhandler) #CTRL-Z

		if self.python_version < 3:
			tempfpath= \
				self.path_current_file.decode(sys.getfilesystemencoding())
		else:
			tempfpath= os.path.realpath(self.path_current_file)

		try:
			#print('Before')
			self.media_info= MediaInfo.parse(tempfpath)	#TODO
			#print('After')
		except:
			print('ERROR: process_media_file')
			return

		cfpath=self.path_current_file
		rfpath=os.path.expandvars(self.path_current_file)
		rfpath=os.path.normpath(rfpath)
		rfname=os.path.basename(rfpath)
		#ahash= zlib.md5()
		#ahash.update(rfpath)
		fpath_hash= zlib.crc32(rfpath)
		fname_hash= zlib.crc32(rfname)
		#self.current_entry= pandas.DataFrame()
#
		# self.current_entry.colums=[\
			# 'total_sec_1970',
			# 'date_sec_1970', \
			# 'date'\
			# 'time', \
			# 'offs', \
			# 'fname', \
			# 'fpath', \
			# 'merged', \
			# 'fname_hash', \
			# 'fpath_hash'
			# ]

		adict= { \
				'total_sec_1970' : 0, \
				'date_sec_1970' : 0, \
			#	'date' : "1970-01-01", \
				'time' : "00:00:00", \
				'offs' : 0, \
				'fname' : rfname,  \
				'fpath' : rfpath, \
				'merged' : False, \
				'fname_hash': fname_hash, \
				'fpath_hash': fpath_hash \
			}
		for self.a_track in self.media_info.tracks: #TODO
			try:
				if self.a_track.track_type == 'General': #TODO
					tr_entries= self.a_track.to_data()
					if self.opt_debug > 1:
						pprint(tr_entries)
					#self.found_date= False

					if tr_entries.has_key('recorded_date'): #TODO
						print("Found %.8192s" % 'recorded_date')
						self.found_date= True
						adatetime= tr_entries['recorded_date']
						andatetime= adatetime[0:19]
						try:
							a_dt= datetime.datetime.strptime( \
								andatetime, \
								self.imp_yyymmddhhmmss_format)
						except:
							print( "ERROR: No correct datetime entry")
							self.found_date= False
							return
						if self.opt_debug > 1:
							print("POS") #TODO LineNr
						total_sec_1970= \
							int((a_dt-self.seconds_since_1970).total_seconds())

						adate= adatetime[0:10] #yyyy-mm-dd
						try:
							a_date= datetime.datetime.strptime(\
								adate, \
								self.imp_yyyymmdd_format)
						except:
							print( "ERROR")

						if self.opt_debug > 1:
							print("line #")#TODO LineNr

						date_sec_1970 = \
							int((a_date-self.seconds_since_1970).total_seconds())

						#yyyy-mm-dd hh:mm:ss+xx:yy
						#0123456789012345678901234
						adate= adatetime[0:10] #yyyy-mm-dd
						atime= adatetime[11:19]
						aoffs= adatetime[20:24]
						fpath_hash= zlib.crc32(rfpath)
						fname_hash= zlib.crc32(rfname)
						#TODO
						#if total_sec_1970 = None or total_sec_1970 == 0:
						#	total_sec_1970= 2012
						adict['total_sec_1970']= total_sec_1970
						adict['date_sec_1970']= date_sec_1970
			#			adict['date']= adate
						adict['time']= atime
						adict['offs']= aoffs
						#resdf=pandas.DataFrame([adict])
						# adict= { \
								# 'total_sec_1970' : total_sec_1970, \
								# 'date_sec_1970' : date_sec_1970, \
								# 'date' : adate, \
								# 'time' : atime, \
								# 'offs' : aoffs, \
								# 'fname' : rfname,  \
								# 'fpath' : rfpath, \
								# 'merged' : False, \
								# 'fname_hash': fname_hash, \
								# 'fpath_hash': fpath_hash \
							# }
						#self.files.append( line )
						#current_row=self.files[ -1:  ]
						self.found_date= True
						#print("DDD")#TODO LineNr
						#print( "%s= %s" % (self.file_counter, \
						#	self.current_entry ))
					else:
						print("-")
			except:
				continue
		resdf=pandas.DataFrame([adict])
		return resdf
						# self.file_log_output.writelines( \
						# self.files[ self.file_counter ] )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def save_json_file(self, dest_path=""):
		return
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def create_json_file_from_dir(self, glob_pattern="./*.m2ts*"):
		global path_default
		global path_json_file
		global do_process
		do_process= True

		#del df['date']
#pandas.DataFrame.drop_duplicates

		#json datei liste
		signal.signal(signal.SIGINT, self.json_signalhandler) #TODO abhängig funktion
		self.path_start_dir= os.path.realpath(glob_pattern)

		if self.opt_verbose > 0:
			print("pattern start dir and filename: %.8192s" \
				% self.path_start_dir)

		self.path_json_file=path_json_file #TODO
		if( len( self.path_json_file ) == 0):
			print('ERROR: No JSON path: "%.8192s"', self.path_json_file)
			sys.exit(-1)
		if self.opt_verbose > 0:
			print('JSON file path: "%.8192s"' % self.path_json_file)
		self.string_glob=glob_pattern	#TODO
		if self.opt_verbose > 0:
			print('Path/Filename Pattern: "%.8192s"' % self.string_glob)
#letzte datei
#alledaieten
		#json file #TODO Resume
		#self.path_json_file="/home/video_output/video_stitch.json" #TODO
		batchcmds= []
		#self.opt_resume_json = False
		if self.opt_resume_json == True:
			try:
				tdf= pandas.read_json(self.path_json_file)
				print(len(tdf))
				temp_df=self.jsonfiles.append( \
					tdf, \
					ignore_index= True, \
					verify_integrity= True)
				self.jsonfiles= temp_df
				print(self.jsonfiles)
				#TODO
				del self.jsonfiles['date']
				print(self.jsonfiles)
				self.jsonfiles.drop_duplicates(keep='first')
				print(self.jsonfiles)

				#print(temp_df)
				print(len(self.jsonfiles))
			except:
				pass
		#self.path_json_file = pandas.read_json('E:/datasets/patients.json')
		#self.path_json_file.head()
			# print('Resume JSON: "%.8192s"' % self.path_json_file)
			# if(os.path.exists(self.path_json_file)):
				# #pandas.options.mode.use_inf_as_na = True
				# #with open('E:/datasets/patients.json', 'w') as f:
				# #	json.dump(patients, f)
				# print("File exists")
				# self.jsonfiles= pandas.read_json(self.path_json_file)
				# try:
					# self.jsonfiles.pandas.read_json(self.path_json_file)
					# self.jsonfiles.head()
					# # with open(self.path_json_file,'r') as f:
						# # #npy=numpy.array
						# # self.jsonfiles= json.load(f)
						# # f.close()
				# except:
					# print("ERROR: No JSON file for resuming - Start new") #TODO
			# #return 0

		# json_counter= len(self.jsonfiles)

			# if self.opt_verbose > -1: #TODO
				# print('JSON Entries #%.256s' % locale_value(json_counter))
				# print("---------------------------------------------------")

		self.file_counter= 0
		#f= open("./video_output/liste.txt",'a+')
		#globs={ 'lastfile': "" }
		#signal.signal(20, json_signalhandler) #CTRL-Z
		ahash = hashlib.md5()
		total_ctr=0
		empty_ctr= 0
		norm_ctr= 0
		do_process= True
		#
		#self.jsonfiles.columns=['']
		glob_results=glob.glob(self.string_glob)
		len_glob=len(glob_results)
		print("Glob res: %s" % len_glob )
		for self.path_current_file in glob_results:
			#screen_clr()
			# # Handling CTRL-C CTRL-Z
			if do_process == False:
				print("...STOPPING!!!!")
				print(len(self.jsonfiles))
				self.jsonfiles.drop_duplicates()
				print(len(self.jsonfiles))
				#print(self.jsonfiles)
				self.save_files_to_json()
				# try:
					# print(self.jsonfiles[89])
					# print(self.jsonfiles[21])
				# except:
					# pass
				sys.exit(0)
			else:
				print("\r...RUNNING...")

			self.path_current_file= \
				os.path.realpath(self.path_current_file)
			bncf= os.path.basename(self.path_current_file)
			crc32_current_path= zlib.crc32(self.path_current_file)
			crc32_current_name= zlib.crc32(bncf)
# #			hash_current_path= ahash.hexdigest()

			# #todo verbose
			if self.opt_verbose > -1: #TODO
				print("...Process file No #%.256s" % locale_value(total_ctr))
				print('...Current file path: "%.8192s"' \
					% self.path_current_file)

			# #f.write('"%.8192"\n' % self.path_current_file)

			# # Check for maximum files read
			if self.file_counter > self.max_files:
				print( 'Reached max read files! EXIT' )
				break
			# if self.opt_verbose > 0:
				# print('...Current file path: "%.8192s"' \
					# % self.path_current_file)
			print('crc32_current_name: %s' % crc32_current_name)
			found= False
			#TODO
			#WICHTIG: Hier mehr auswahl kriterien dateiname, totalsec, dateihash
			# oder gar AI Algo
			for a in self.jsonfiles['fname_hash']:
				#if debug
				#print("json entry fn  hash %s - file #%s crc32 name hash %s" % (a, total_ctr,crc32_current_name))

				#skip= True
				if crc32_current_name == a:
					print("json entry fn  hash %s - file #%s crc32 name hash %s" % (a, total_ctr,crc32_current_name))
					print('# %s already in DB "%s"!' % (total_ctr, self.path_current_file))
					found= True
					skip= True
					break

			if found == False:
				print(self.path_current_file)
				media_info_res= self.process_media_file()	#TODO Hier dauerts
				#pprint.pprint(media_info_res)
				if self.found_date == False:
					print('\n\nERROR: NO record date in file "%.8192s"' \
						% self.path_current_file)
					print('...SKIPPING FILE!!!')
					empty_ctr+=1
					skip= True
					break
				else:
					skip= False
			if skip == False:
				print("json entry fn  hash %s - file #%s crc32 name hash %s" % (a, total_ctr,crc32_current_name))
				print('Adding "%s"!' % self.path_current_file)
				tmp=\
					self.jsonfiles.append(\
						media_info_res, \
						ignore_index= True, \
						verify_integrity= True)
				self.jsonfiles=tmp
				self.jsonfiles.drop_duplicates(keep='first')
				skip= False
				norm_ctr+=1

			total_ctr+=1
			if ( total_ctr % 200 ) == 0:
				self.save_files_to_json()

				#self.save_files_to_json(self.path_json_file)

		print("FINISHED JSON File!")
		print(self.jsonfiles)
		#self.save_files_to_json(self.path_json_file)
		self.save_files_to_json()
						# #inode=int(bn[1:10]) #TODO
						# #print('...INODE: %.200s' % locale_value(inode))
						# its=int(res['total_sec_1970'])
						# ts=locale_value(its)
						# print()
						# print('...NR. NEW FILE: %20s' % locale_value(l) )
						# # datetime.datetime.fromtimestamp(1284286794)
						# print( datetime.datetime.fromtimestamp(its).strftime('%Y-%m-%d %H:%M:%S'))
						# print('...TOTAL SEC SINCE 1970: %.200s' % ts)
						# print(its)
						# print('...ADDING ENTRY!!!!:\n')
						# pprint(res)
						# #sys.stdout.flush()
		return 0
#=======================================================================
	def test_json_integrity(self):
		global path_json_file
		self.path_json_file= path_json_file
		if(os.path.exists(self.path_json_file)):
			with open(self.path_json_file,'r') as f:
				self.jsonfiles= json.load(f)
				f.close()
		self.jsonfiles.sort(key=itemgetter('fpath'))
		result= self.jsonfiles.sort(key=itemgetter('fpath'))
		for entry in sorted(self.jsonfiles):
			print(entry['fpath'])
		print( 'JSON Entries #%.8192s' % locale_value(len(self.jsonfiles)))
		# r= json.dumps(self.jsonfiles, indent=3)
		# f = open('./sample.json', 'a+')
		# print(r,f)
		# f.close()
		print("\n\n###################################################")
		seen = set()
		new_l = []
		for d in self.jsonfiles:
			t = tuple(sorted(d.items()))
			if t not in seen:
				seen.add(t)
				new_l.append(d)
		#pprint(new_l)
		print(len(new_l))
		f = open('./sample.json', 'a+')	#TODO
#		r= json.dumps(new_l, indent=3)
		#print(r,f)
#		f.close()
		#ANdere noch kürzere
		print("\n\n###################################################")
		print("\n\n###################################################")
		print("\n\n###################################################")

		entries= [dict(t) for t in {tuple(sorted(entry.items())) \
			for entry in self.jsonfiles}]
		for entry in sorted(entries):
			print(entry['fpath'])
		print(len(entry))
#=======================================================================
	def signal_test(self):
		print("atest")
#=======================================================================
	def kill_encoder_proc(self):
		subprocess.call(['killall', '-s', '9', 'mencoder'])
		subprocess.call(['killall', '-s', '9', 'python'])
#=======================================================================
# #mencoder  -ni -msgcolor  -oac copy -ovc h264 -o '/home/user/video_output/1525996800.mp4'  "/nas0030/data20200208/recovered2/n29/f290007467_pid_0.m2ts"  "/nas0030/data20200208/recovered2/n29/f290007467_pid_0.m2ts_20200402"  "/nas0030/data20200208/recovered2/n29/f290228917_pid_0.m2ts"  "/nas0030/data20200208/recovered2/n29/f290228917_pid_0.m2ts_20200402"  "/nas0030/data20200208/recovered2/n29/f290296521_pid_0.m2ts"  "/nas0030/data20200208/recovered2/n29/f290296521_pid_0.m2ts_20200402"
	def process_json_datafile(self, path_json_file):
		global do_process
		global path_dir_output
		global merge_method
		batchcmds=[]
		merge_method= 1
		print("------------------------- PROCESS JSON ----------------")
		if self.opt_debug > 1:
			print("Merge method: %i" % self.merge_method )
		self.merge_method= merge_method
		self.path_json_file=path_json_file #TODO
		self.mrgcmds= []
		print(os.path.realpath(self.path_json_file))
		if self.opt_verbose > 0:
			print('Parsing JSON File "%.8192s"' % self.path_json_file)
		result= 0
		data=""

		# if len(self.files) == 0:
			# self.files = {}
		# Read JSON File
		#TODO
		#jsonfiles
		#self.files= pandas.DataFrame()
		self.json_file_already_loaded= False
		if self.json_file_already_loaded == False:
		# with open(self.path_json_input, 'r') as f:
			try:
				self.files= pandas.read_json(self.path_json_file)
			except:
				print('ERROR: Can NOT load json File "%s"' \
					% self.path_json_file)
				sys.exit(-1)
			print( "... Nr. Entries: %s" \
				% locale_value( len(self.files) ) )
			if self.opt_debug > 7:
				pprint(self.files)
		print('... JSON File "%.8192s" SUCCESFULY loaded' \
			% self.path_json_file)
		# except:

		c= 0
		if self.opt_verbose > 3:
			for df_entry in self.files:
				print("ENTRY->%.256s" % locale_value(c))
				pprint.pprint(df_entry)
				c+=1

		#Multiprocessing
		# self.pool_size = multiprocessing.cpu_count()
		# self.pool = multiprocessing.Pool(
			# processes=self.pool_size,
			# initializer=start_processes,
			# maxtasksperchild= 2
			# )
		ic=0
		#merging
		self.mrgcmds= []

		if self.opt_verbose > 0:
			print('...Merging now')
		print("--------------------------------------------------")

		df= self.files
		#for gentry in self.files.groupby('date_sec_1970')[['fpath','total_sec_1970']]:

		###### TODO Python for Professionals S 119 Itemgetter, lambda
		###### und lst to set
		grouped =df.groupby('date_sec_1970')
		print(len(grouped))
		gc= 0
		alines=[]
		agroup=[]
		self.agroups=[]  #g    l     c
		#agroups=[0..1][0..n][fpath..]
		print(gc) #TODO spalten zu zeilen -> listen (i, fpath, totalsec, datesec)
		cmdgroups=[]
		sAll_cmdlines="#!/bin/bash\n" + "rm /home/user/alog.txt\n"
		grp_cmdlines=""
		sConcat_cmdlines=""
		sLog_cmdline=" 2>&1 | tee -a /home/user/alog.txt\n"
		for name, df_group in grouped: # TODOsinnvoll da row=line?
			#DEBUG: \
			#print('ID: ' + str(name))
				#DEBUG: \
			#for index, row in df_group.iterrows(): !!!
			self.acmdgroup=[]
			agroup=[]
			acmdline=[ 'mencoder' ]
			scmdline_L1p1="/usr/bin/ffmpeg "
			yfg=[]
			scmdline_L1p2=""
			sGrp_cmdlines=""
			sFiles_cmdline=""
			sCmdline= "" \
				+ '/usr/bin/ffmpeg -err_detect ignore_err ' \
				+ '-i concat:'
			for name, row in df_group.iterrows():
				#DEBUG: \
				#row=line=y, column=x
				y= row
				index= name
				datesec= y['date_sec_1970']
				destname='%s.mp4' % datesec
				destpath='/ddisk/%s' % destname
				totalsec= y['total_sec_1970']
				ifPath= y['fpath']
#				bifname= os.path.basename(ifPath)
#				fNewPath='/mts_sourcefiles/%.10s.m2ts' % bifname # wg fxxxxxxxxx.m2ts #TODO
				fNewPath='%.255s' % ifPath # wg fxxxxxxxxx.m2ts #TODO
				#DEBUG: \

				#'NEUUU

				#ffmpeg -i concat:"videoclip1.mpg|videoclip2.mpg" -c copy video.mpg
				#S180 ffmpeg basics
				sFiles_cmdline+="%s|" % fNewPath
				#sXFiles_cmdline='if [[ ! -s "%s" ]]; then ' % fNewPath
				#scmdline_L1p2+= "%s " % fpath
				yfg.append(ifPath)
				#DEBUG: \
				#cmdline.append(fpath)
				ay={'destpath': destpath, \
					'destname': destname, \
					'desttname': 0, \
					'totalsec': totalsec, \
					'fpath': ifPath}
				if ay != None:
					agroup.append(ay)
					#DEBUG: \
					#pprint.pprint(aline)
					#print("added aline")
					#print("!!!")
					#agroup= agroup.sort()
				#DEBUG: \
				#print('{index %s, datesec: %i, fpath "%s", totalsec: %i}' \
				#	% (index, datesec, fpath, totalsec))
			sFiles_cmdline=sFiles_cmdline[0:-1]
			sCmdline+='"%s" ' % sFiles_cmdline
			sCmdline+= \
				'-n ' \
				+ '-c:v copy ' \
				+ '-c:a aac ' \
				+ '-b:a 128k ' \
				+ '-psnr ' \
				+ '-fpsprobesize 1000 ' \
				+ '-analyzeduration 50000000 ' \
				+ '-start_at_zero ' \
				+ '-copyts ' \
				+ '-copy_unknown ' \
				+ '-copytb 1 '\
				+ '-r 25 ' \
				+ '"%s" ' % fNewPath
			sCmdline+= sLog_cmdline
			sCmdline+= \
				'\necho "##########################################"\n'
			sGrp_cmdlines+=sCmdline

			#batch
			#for sopt in self.mrgcmd_opt_all_file[1]:
			#	scmdline_p1+= sopt + ' '
#			scmdline_L1p1+=\
#				"ffmpeg -i '$i' -vcodec mpeg4 -b:v 15M -acodec libmp3lame -b:a 192k"
				#"ffmpeg -i '$i' -vcodec mpeg4 -b:v 15M -acodec libmp3lame -b:a 192k"
			# scmdline_p1+= \
				# '-cache ' + str(mencoder_cachesize) + ' -ovc x264 ' + \
				# '-oac lavc -lavcopts acodec=aac:abitrate=128'
#			sCurfinalcmdline='/usr/bin/mencoder -oac copy -ovc copy -o "%s" ' % destpath
#			sCurfinalcmdline+= sfilescmdline
			sConcat_cmdline=""
			#sConcat_cmdline='echo "##########################################"\n'
			#sConcat_cmdline+='/usr/bin/mencoder -oac copy -ovc copy -o "%s" \\\n' % destpath
			sConcat_cmdline+= sFiles_cmdline
			sConcat_cmdline+= sLog_cmdline
			#print(str(datesec).center(24, "#"))

						#scmdline_L1P2+=' -o "%s-x264.avi" ' % destname
			#scmdline= scmdline_p1 + scmdline_p2
			#scmdline+= "\necho '###################################'"

#			sGrp_cmdlines+="\n" + sConcat_cmdline
			sGrp_cmdlines+="\n"

			#tgrp_cmdlines+="\n" + sCurfinalcmdline
			sGrp_cmdlines+= "\necho '^^^" + destpath.encode('ascii','replace').center(50, str("#"))+"^^^'\n\n"
			print(sGrp_cmdlines)
			print(sConcat_cmdlines)
			sAll_cmdlines+= 'cd /ddisk\n' + sGrp_cmdlines
			#sConcat_cmdlines+= "\n" + sConcat_cmdline
			#all_cmdlines+= 'cd /ddisk\n' +tgrp_cmdlines
			#scmdline+=

			# python multicore
			self.asgroup= sorted(agroup, key=itemgetter('totalsec'))
			acmdline.append('-o')
			acmdline.append(destname)
			acmdline.extend(sorted(yfg))
			self.acmdgroup.append(acmdline)
			#pprint.pprint(acmdline)
			self.agroups.append(self.asgroup)
			print("---------------------------------------------")
			#time.sleep(5)

		sAll_cmdlines+= sConcat_cmdlines
		#pprint.pprint(agroup)
		ctr=0
		#Batch file
		#pprint.pprint(self.acmdgroup)
		with open('/home/user/videobatchfile.sh', 'w') as x:
			#for line in self.acmdgroup:
			x.write(sAll_cmdlines)
			x.close()
		if self.opt_stop_before_encoding == True:
			#Changed heute
			self.pool.terminate()
			sys.exit(0)
			pass
		#do_process= False
		sys.exit(-1)
		if do_process == False:
			#Changed heute
			self.kill_encoder_proc()
			self.pool.terminate()

		print("... running now in multiprocessing")

		if do_process == True:
			self.kill_encoder_proc()
			self.pool_outputs = self.pool.imap_unordered(worker, self.acmdgroup)
			self.pool_outputs = self.pool.map(worker, self.acmdgroup)
			self.pool.close()
			self.pool.join()
			while do_process == True:
				pass
		else:
			self.kill_encoder_proc()

		sys.exit(-1)
		# #pydoc.pager(astr)

	# #	sys.exit(-1)
# #		pydoc.pager(astr)

				# #pprint(command_line)
# #		pydoc.pager(astr)			#time.sleep(5)


		# #print(batchcmd)
			# #jetzt


		# #TODO test auf output verzeichnis
		# if self.opt_verbose > 0:

		return  #TODO
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def create_batch_from_json_file(self):
		""" Function doc """
		return 0
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def sort_and_reduce_json(self):
		# new_l= [dict(t) for t in {tuple(sorted(entry.items())) for entry in self.jsonfiles}]
		# self.jsonfiles=new_l[0:]
		# print("sux")
		# pprint( self.jsonfiles[0] )
		# #pprint(self.jsonfiles)
		return 0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#=======================================================================
	def debug_create_emptyfiles(self):
		glob_results=glob.glob('/finished/*.mp4') #todo
		ctr= 0

		for ap in glob_results:
			rp= os.path.realpath(ap)
			bn= os.path.basename(ap)
			ndp= os.path.realpath('./video_output/')
			np= os.path.join(ndp, bn)
			#backup_file(rp,

			print(np)
			with open(np,'w') as f:
				f.write('\n')
				f.close()
		return 0
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


######################################################################
	# def parse_options( self, argv ):
		# try:
			# opts, args= getopt.getopt(
				# [
					# sys.argv[1:],
					# 's:d:j:vV',
					# ’--sourcedir’, ’val’,
					# ’--witharg2=another’,
				# ],
				# ’’,
				# [ ’noarg’, ’witharg=’, ’witharg2=’ ])
		# except:
				# for opt in opts:
					# print opt
		# vers= sys.version_info.major
		# print("Python Vers %s" % vers)
		# if len(sys.argv) == 1:
			# print("Usage: {} <filename/path-pattern>".format(sys.argv[0]))
			# apath_pattern= default_path_pattern
		# else:
			# apath_pattern = sys.argv[1]
			# pass

	def backup_file(self, filepath, destdir="./"): #TODO
		backup_dir_path=os.path.realpath(destdir)
		tpath=os.path.realpath(filepath)
		backup_name_we=os.path.basename(tpath)
		backup_name_woe=os.path.splitext(backup_name_we)[0]
		backup_dir=os.path.dirname(tpath)
		backup_path=\
			os.path.join("%.8192s" % backup_dir_path, \
			"%.8192s.json.bak" % backup_name_woe)
		try:
			shutil.copyfile(tpath, backup_path)
			result= 0
		except:
			result= -1
		return result
######################################################################
	def avifix(self):
		return
######################################################################
	def parse_options( self, argv ):
		if len(sys.argv) == 1:
			print("Usage: {} <filename/path-pattern>".format(sys.argv[0]))
			sys.exit(-1)

		try:
			opts, args= getopt.getopt(
				[
					sys.argv[1:],
					's:d:j:b:e:c:v:Vfwhr',
					'--sourcedir=',
					'--destdir=',
					'--jsonpath=',
					'--encodingtype=',
					'--batchpath=',
					'--finishedlistpath=',
					'--verbosity=',
					'--resumejson',
					'--nosound',
					'--Version',
					'--force',
					'--help',
				])
		except:
			sys.exit(-2)
#			self.opt_photorec
		for opt in opts:
			if opt in ( '-s', '--sourcedir'):
				self.path_start_dir= ""
				continue
			elif opt in ( '-d', '--destdir'):
				self.path_dir_output= ""
				continue
			elif opt in ( '-j', '--jsonpath'):
				self.opt_
				continue
			elif opt in ( '-e', '--encodingtype'):
				continue
			elif opt in ( '-b', '--batchpath'):
				self.opt_batchfile=""
				continue
			elif opt in ( '-l', '--finishedlistpath'):
				continue
			elif opt in ( '-f', '--force'):
				self.opt_overwrite= True
				continue
			elif opt in ( '-c', '--enccommand'):
				continue
			elif opt in ( '-v', '--verbosity'):
				self.opt_verbose= 0
				continue
			elif opt in ( '-V', '--Version'):
				continue
			elif opt in ( '-w', '--'):
				continue
			elif opt in ( '--nosound'):
				self.opt_photorec= True
				continue
			elif opt in ( '-p', '--photorec'):
				self.opt_photorec= True
				continue
			else:
				print("ERROR: Unknown Option - EXIT!")
				sys.exit(-2)
			print(opt)
		#vers= sys.version_info.major
		#print("Python Vers %s" % vers)
#=======================================================================
def z_main():
	return
#=======================================================================
def print_help():
	return
#=======================================================================
if __name__ == "__main__":
	global MediaInfo
	global default_path_pattern
	#global path_json_file

	#avideostitcher= videostitcher("/adisk/recovered_high/") #TODO mkdir
	avideostitcher= videostitcher(path_dir_output) #TODO mkdir
	#avideostitcher.parse_options(self, argv)
	object_self= avideostitcher
	#if avideostitcher.opt_debug > 7:
	#	avideostitcher.test_json_integrity()
	#if do_json_parse == True: #TODO
	path_json_file="/home/video_output/video_stitch.json"
	avideostitcher.path_json_file=path_json_file
	#avideostitcher.create_json_file_from_dir(default_path_pattern)
	#sys.exit(1)
	do_process_json= True
	if do_process_json == True:
		print(path_json_file)
		avideostitcher.process_json_datafile(path_json_file)
	#avideostitcher.debug_create_emptyfiles()
	#avideostitcher.process_dir(apath_pattern) #recusiv flag
	sys.exit(0)

# <TRASH>
			# #merged = [{**d1, **d2} for d1, d2 in zip(data1, data2)]
			#TODO Bessere suche nach doppelten
			#TODO
			# #jpath= self.jsonfiles[0]['fpath']
			# while True:
				# ctr+=1
				# jpath= itemgetter(self.jsonfiles['total_sec_1970'])
				# print(jpath)
				# if self.path_current_file == jpath:
					#print('File "%.8192s" already exists in JSON!!!!!!!' % jpath)
					# skip= True
					# break
# def search_dict(my_dict,searchFor):
    # s_val = [[ k if searchFor in v else None for v in my_dict[k]] for k in my_dict]
    # return s_val
#
#search_dict = lambda x, y: ((k if y in v else None for v in x[k]) for k in x)
				#jpath=jsonentry['fpath']


					# afiles= { '000000': [ { 'datum01': 0, 'wert': 1 }, {'datum03': 1, 'wert': 2 } ], '00001': [ 'c', 'd'] }
	# #pprint(afiles)
	# for adate1970 in afiles.keys():
		# nl=afiles.get(adate1970)
		# print( len(nl))
		# nl.append({'datum_x': 2 })
		# afiles[adate1970]=nl
		# #afile.update({'datum_x': 2, 'wert': 9})
		# #afile.update(akey, nl)

	# for akey in afiles.keys():
		# print(akey)
		# entries= afiles.get(akey)
# #		nl=afiles.get(akey)
# #		nl.append({'datum_x': 2, 'wert': 9})
		# #afiles.update(akey, nl)
		# for entry in entries:
			# pprint(entry)
		# #pprint(afiles.get(akey))# for ae in afile:
			# # print(ae)
					# for date_sec_1970, entries in groupby(self.files, key=itemgetter('date_sec_1970')):
			# mrgcmd= []
			# sys.stdout.write("...Running")
			# print('')
			# if merge_method > self.num_merge_methods:
				# print('ERROR: invalid merge method="%.255s"' %
					# merge_method )
				# sys.exit(-2)#TODO
			# #print(merge_method)

			# # Add options to merge command
			# if self.opt_debug > 0:
				# print("...opts:")
			# for opt in self.mrgcmd_opt_all_file[merge_method]:
				# #pprint(opt)
				# if self.opt_verbose > 9:
					# print('opt %.8192s' % opt)
				# mrgcmd.append( opt )

			# if self.opt_debug > 2:
				# print('Finished Options')

			# self.files2concat= 0
			# optctr=0

			# # Create output file name #TODO date as name
			# self.path_dir_output=path_dir_output #TODO
			# self.fname_output='%.8192s%.8192s' % \
				# (date_sec_1970, self.mrg_ext)
			# self.cpath_file_output=\
				# os.path.join( \
				# self.path_dir_output, \
				# '%.8192s' % self.fname_output )
# #				'%.8192s%.8192s' % (date_sec_1970, self.mrg_ext))
			# print('...Output file="%.8129s"' % self.cpath_file_output)

			# #Problematic files
			# if str(date_sec_1970) in errfiles:
				# #sys.exit(-1)
				# break
				# #sys.exit(1)#todo

			# # Check whether output file is already there
			# if os.path.exists(self.cpath_file_output) == True:
				# if self.opt_overwrite == False:
					# print('INFO: File "%.8192s" exists - SKIPPING!!!\n'
						# % self.cpath_file_output)
					# continue
			# print('... INFO: using mencoder') #TODO
			# print('output %.8192s' % self.cpath_file_output)
			# mrgcmd.append('-o')
			# mrgcmd.append('%.8192s' % self.cpath_file_output)

			# # Input file loop	TODOhashing filename
			# fc= 0
			# for entry in entries:
				# try:
					# cdate_sec_1970=entry['date_sec_1970']
					# cfpath=entry['fpath']
				# except:
					# do_process= False
			# #Changed heute
					# #sys.exit(-2) #TODO
				# if cfpath in errfiles:
					# print("ERRFILE")
				# #	do_process= False

				# #if do_process == False:
					# # todo opt_debug
				# #	print("...Stopping!!!!\n\n")
				# #	break
				# fc+= 1
				# #print()
			# #	if int(cdate_sec_1970) < date_sec_start:	#TODO
			# #		continue
# #os.path.getsize(__file__)
				# if self.opt_debug > 4:
					# encoder_cmd= amrgcmd_base[merge_method]
					# mrgcmd.append(encoder_cmd)
					# print('...encoder_cmd="%.8192s"' % encoder_cmd)
					# print(batchcmd)

			# #Output file pos for MENCODER
				# merge_method= 1	#TODO
				# tpath=""
				# total_sec_1970=entry['total_sec_1970']
				# #if self.opt_debug > 2:
				# #	print("...JSON ENTRY: total_sec=%.8192s" \
				# #		% locale_value(total_sec_1970))
				# if os.path.exists(cfpath) == True:
					# if merge_method == 1: #mencoder # TODO
						# tpath="%.8192s" % cfpath
						# if self.opt_debug > 4:
							# print('...Temppath="%.8192s"' % tpath)
						# #ctr+= 1
						# entry['merged']= True
						# #if self.opt_verbose > -1:
						# #pprint( #TODO
						# if optctr == 0:
							# #mrgcmd.append("--load")
							# mrgcmd.append("%.8192s" % tpath)
						# else:
							# opt_per_file= self.mrgcmd_opt_per_file[merge_method][0]
						# #or opt_per_file in self.mrgcmd_opt_per_file[merge_method]:
						# #	print(opt_per_file)
							# #mrgcmd.append( opt_per_file )
							# mrgcmd.append("%.8192s" % tpath)
						# entry['merged']= True
						# self.files2concat+= 1
						# #optctr+= 1
					# elif merge_method == 2:
						# #ctr+= 1
						# sm="|"
						# tpath= tpath + '|' + fpath
						# entry['merged']= True
						# self.files2concat+= 1
					# else:
						# print('ERROR: No merge method!!!')
						# self.files2concat= 0
						# do_process= False
						# sys.exit(-2)
				# else:
					# print("ERROR: Partial File not exists '%.8192s'" % cfpath)
				# # TODO
				# # if merge_method == 2:
					# # mrgcmd.append('-i')
					# # mrgcmd.append('...Concat="%.32768s"' % tpath[1:])

				# #TODO
				# if self.files2concat <= 0:# TODO
					# print('ERROR: No files 2 concat')
					# #time.sleep(5)
# #					sys.exit(-2)
				# # if(self.opt_batchfile):
					# # batchcmd+= '%.8192s ' % cfpath

				# if self.opt_debug > 0:
					# print("... Nr. Files to concat=%.200s" \
						# % locale_value(self.files2concat))

			# if date_sec_1970 in errfiles:
				# # print('###############################################')
				# # print("ERROR FILE found!!!")
				# # print (self.fname_output)
				# # pprint(mrgcmd)
				# # do_process= False;
				# # self.pool[-1].terminate()
				# print("ERROR FILE found!!!")
				# # sys.exit(-2)
			# #Changed heute

				# # #subprocess.call(['killall', '-s', '9', 'mencoder'])
# # #				subprocess.call(['killall', '-s', '9', 'python'])
				# # sys.exit(-2)
				# # break
			# #ENDE Dateischleife

			# #Output file path
			# self.path_dir_output=path_dir_output #TODO
			# self.cpath_file_output=\
				# os.path.join( \
				# self.path_dir_output, \
				# '%.8192s%.8192s' % (date_sec_1970, self.mrg_ext))

			# #Check whether file exists
			# if os.path.exists(self.cpath_file_output) == True:
				# if self.opt_overwrite == False:
					# print('INFO: File "%.8192s" exists - SKIPPING!!!\n'
						# % self.cpath_file_output)
			# else:
				# print

				# if self.files2concat > 0:
					# print("--------------------")

					# if merge_method == 1:	#TODO
						# self.mrgcmds.append(mrgcmd)
						# ctr+= 1

					# elif merge_method == 2:
						# print('... INFO: using avidemux')
						# mrgcmd.append('--save')
						# mrgcmd.append('%.8192s' % self.cpath_file_output)
						# #batchcmd+='-o "%.8192s"' % cpath_file_output

						# #ctr+= 1
						# self.mrgcmds.append(mrgcmd)
						# if self.opt_debug > 4:
							# pprint(mrgcmd)
							# #print(batchcmd)
					# else:
						# nix=0

					# # Batch file
					# if(self.opt_batchfile) == True:
						# #batchcmd.append('-append "%.8192s"' % self.cpath_file_output)
						# # for opt in mrgcmd:
							# # print(opt)

						# with open("./video_output/mergecmds.sh", 'a+') as f: #TODO
							# f.write("reset; mencoder " )
							# for opt in mrgcmd:
								# f.write("%.16384s " % opt)
							# f.write("\n")
							# f.close()
						# #batchcmds.append(batchcmd)
					# print("mergecmd No.:%.8192s" \
						# % locale_value(ctr))
					# pprint(mrgcmd)
					# print("===========================================")
					# ctr+= 1
					# #print(batchcmd)
#</alt>

					#print("json")
					# print("totalsec1970")
					# x=[]
					# x= self.jsonfiles['total_sec_1970'][0:]
					# tse=  media_info_res['total_sec_1970']
					# print('xl:%s' % len(x))
					# print('tse:%32s' % tse[0])
					# pprint.pprint(x[0:][1:])

					# print("-")
					# if (tse.isin(x).any())== True:
						# print("dup!:%s" % self.path_current_file)
						# print("File already in DB")
						# self.skip
			#pandas.series(media_info_res)
			#columns=['a','b','c','d'], index=['x','y','z'])
			#index[0..len(self.
			#df= pandas.DataFrame([media_info_res])
			#pandas.DataFrame.from_dict(media_info_res, orient='index',columns=['A', 'B', 'C', 'D'])
			#time.sleep(5)
