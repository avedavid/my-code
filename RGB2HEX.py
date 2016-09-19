def rgb_hex():
  
  INVALID_MSG='The value you have entered is invalid, try again.'
  
  r=int(raw_input('Enter an intensity value from 0 to 255 for Red: '))
  if r<0 or r>255:
    print INVALID_MSG
    return
  
  g=int(raw_input('Enter an intensity value from 0 to 255 for Green: '))
  if g<0 or g>255:
    print INVALID_MSG
    return
  
  b=int(raw_input('Enter an intensity value from 0 to 255 for Blue: '))
  if b<0 or b>255:
    print INVALID_MSG
    return
  val=(r<<16) + (g<<8) + b
  print (hex(val)[2:]).upper()
  
def hex_rgb():
  hex_val=raw_input('Enter a hexadecimal value for your color: ')
  if len(hex_val)!=6:
    print 'Invalid input'
    return
  val=int(hex_val, 16)
  r=val>>16
  p=val-(r<<16)
  g=p>>8
  b=p-(g<<8)
  print '(%d,%d,%d)' %(r,g,b)
  
def convert():
  while True:
    option=int(raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter 3 to Exit: '))
    if option==1:
      print 'RGB to HEX...'
      rgb_hex()
    elif option==2:
      print 'HEX to RGB...'
      hex_rgb()
    elif option==3:
      break
    else:
      print "Invalid input, try again"
      
convert()      
      
    
  
  
  
    
