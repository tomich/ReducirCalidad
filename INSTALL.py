#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import os, sys
import shutil
import pygtk, gtk
#
#info=gtk.MessageDialog(message_format="Archivo exportado correctamente en formato desconocido.")
        
#    info.run()
#    info.destroy()

origen=(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"")+'u-data/')
nautilusdir=os.path.expanduser('~')+ '/.gnome2/nautilus-scripts/'
sys.path.insert(0,origen)
import Process
def checkorigen():
	ans=1
	if not os.path.exists(origen):
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="No se encuentra directorio u-data")
		ans=0
	if not os.path.isfile(origen + "Process.py"):
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="No se encuentra archivo Process.py en directorio u-data")
		ans=0
	if not os.path.isfile(origen + "ReducirCalidad"):
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="No se encuentra archivo ReducirCalidad en directorio u-data")
		ans=0
	if ans==0:
		info.run()
		info.destroy()
		sys.exit()
	

def copiar_archivos():
	if os.path.exists(nautilusdir):
		try:
			shutil.copy2(origen + "Process.py" , nautilusdir + "Process.py")
			shutil.copy2(origen + "ReducirCalidad" , nautilusdir + "ReducirCalidad")
		except:
			info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="Error copiando archivos")
			info.run()
			info.destroy()
			sys.exit()
	else:
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="Directorio Destino no existe")
		info.run()
		info.destroy()
		sys.exit()
def configurar_permisos():
	try:	
		insdirproc=str(nautilusdir) + "Process.py"
		insdirred=str(nautilusdir) + "ReducirCalidad"
		os.chmod(insdirproc,0666)
		os.chmod(insdirred,0777)
	except:
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="Error aplicando permisos, pero deberia funcionar de todas formas")
		info.run()
		info.destroy()
		sys.exit()

def instalar_image():
	try:
		os.system('gksudo apt-get install imagemagick')
	except:
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="Error al instalar Imagemagick")
		info.run()
		info.destroy()
		sys.exit()

def festejar():
	info=gtk.MessageDialog(buttons=gtk.BUTTONS_OK,message_format="Correctamente instalado")
	info.run()
	info.destroy()

def checkinstall():
	if Process.verifyCommands("convert%ImageMagick")==False:
		info=gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,message_format="Error al instalar Imagemagick")
		info.run()
		info.destroy()
		sys.exit()
def consulta():
	sino = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION,buttons=gtk.BUTTONS_YES_NO, message_format="Esto instalara 'ReducirCalidad' a los scripts de Nautilus. Es posible que se le pida clave de root para instalar dependencias.¿Desea continuar?")
	duda=sino.run()
	if duda==gtk.RESPONSE_NO:
		sino.destroy()
		sys.end()
	sino.destroy()

checkorigen()
consulta()
instalar_image()
checkinstall()
copiar_archivos()
configurar_permisos()
festejar()


