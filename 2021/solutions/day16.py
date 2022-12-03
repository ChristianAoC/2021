#input = [[int(x) for x in line.strip()] for line in open('inputs/16test.txt', 'r')]

### TASK 1

htobdict = {
  "0": "0000",
  "1": "0001",
  "2": "0010",
  "3": "0011",
  "4": "0100",
  "5": "0101",
  "6": "0110",
  "7": "0111",
  "8": "1000",
  "9": "1001",
  "A": "1010",
  "B": "1011",
  "C": "1100",
  "D": "1101",
  "E": "1110",
  "F": "1111"
}

inputfull = "2056FA18025A00A4F52AB13FAB6CDA779E1B2012DB003301006A35C7D882200C43289F07A5A192D200C1BC011969BA4A485E63D8FE4CC80480C00D500010F8991E23A8803104A3C425967260020E551DC01D98B5FEF33D5C044C0928053296CDAFCB8D4BDAA611F256DE7B945220080244BE59EE7D0A5D0E6545C0268A7126564732552F003194400B10031C00C002819C00B50034400A70039C009401A114009201500C00B00100D00354300254008200609000D39BB5868C01E9A649C5D9C4A8CC6016CC9B4229F3399629A0C3005E797A5040C016A00DD40010B8E508615000213112294749B8D67EC45F63A980233D8BCF1DC44FAC017914993D42C9000282CB9D4A776233B4BF361F2F9F6659CE5764EB9A3E9007ED3B7B6896C0159F9D1EE76B3FFEF4B8FCF3B88019316E51DA181802B400A8CFCC127E60935D7B10078C01F8B50B20E1803D1FA21C6F300661AC678946008C918E002A72A0F27D82DB802B239A63BAEEA9C6395D98A001A9234EA620026D1AE5CA60A900A4B335A4F815C01A800021B1AE2E4441006A0A47686AE01449CB5534929FF567B9587C6A214C6212ACBF53F9A8E7D3CFF0B136FD061401091719BC5330E5474000D887B24162013CC7EDDCDD8E5E77E53AF128B1276D0F980292DA0CD004A7798EEEC672A7A6008C953F8BD7F781ED00395317AF0726E3402100625F3D9CB18B546E2FC9C65D1C20020E4C36460392F7683004A77DB3DB00527B5A85E06F253442014A00010A8F9106108002190B61E4750004262BC7587E801674EB0CCF1025716A054AD47080467A00B864AD2D4B193E92B4B52C64F27BFB05200C165A38DDF8D5A009C9C2463030802879EB55AB8010396069C413005FC01098EDD0A63B742852402B74DF7FDFE8368037700043E2FC2C8CA00087C518990C0C015C00542726C13936392A4633D8F1802532E5801E84FDF34FCA1487D367EF9A7E50A43E90"

input1 = "D2FE28"
input2 = "38006F45291200"
input3 = "EE00D40C823060"
input4 = "8A004A801A8002F478" #16
input5 = "620080001611562C8802118E34" #12
input6 = "C0015000016115A2E0802F182340" #23
input7 = "A0016C880162017C3686B18A3D4780" #31
vsum = 0

def conv_input(inp):
  bininput = ""
  for char in inp:
    bininput += htobdict[char]
  return bininput

"""
def pack_type(arg, vsum):
  if len(arg) > 10:
    vsum += int(arg[0:3],2)
    #print("version: "+str(int(arg[0:3],2)))
    pid = int(arg[3:6],2)
    if(pid == 4):
      literal_value(arg[6:], vsum)
    else:
      print("operator"+arg[6:])
      operator(arg[6:], vsum)
      if int(arg[0:3],2) is not None:
        vsum += int(arg[0:3],2)
    return vsum

def literal_value(arg, vsum):
  val = ""
  while True:
    val += arg[0:5]
    if arg[1] == "0":
      break
    arg = arg[5:]
  print("Literal value: "+str(int(val,2)))

  lit = arg
#  print(arg)
#  while len(arg)%4 != 0:
#    arg = "0"+arg
#  arg = arg.rstrip('0')
#  print(arg)
# FIX THIS !!!!!
#  val = ""
#  stop = False
#  while len(arg) > 5 and stop == False:
#    if arg[1] == "0":
#      stop = True
#    val += arg[:5]
#    arg = arg[5:]
#    print("Literal value: "+str(int(val,2)))
#  if len(arg) > 11 and stop == True:
#    vsum += pack_type(arg[16:27], vsum)

def operator(arg, vsum):
  ltid = arg[0:1]
  print("tlid "+ltid)
  if ltid == "0":
    bitlen = int(str(arg[2:16]),2)
    if bitlen > 11:
      vsum += pack_type(arg[16:27], vsum)
      vsum += pack_type(arg[27:27+bitlen-11], vsum)
    else:
      vsum += pack_type(arg[16:16+bitlen], vsum)
  elif ltid == "1":
    numpacks = int(str(arg[2:12]),2)
    print("numpacks "+str(numpacks))
    for i in range(numpacks):
#      print(arg[15+i*11:26+i*11])
#      print(12+i*11)
#      print(23+i*11)
      if i == numpacks-1:
        vsum += pack_type(arg[12+i*11:], vsum)
      else:
        vsum += pack_type(arg[12+i*11:23+i*11], vsum)
"""

#vsum = pack_type(bininput, vsum)
#print("Task 1 - sum of all version numbers: "+str(vsum))

#print("input 1:")
#print(pack_type(conv_input(input1), 0))
#print("input 2:")
#print(pack_type(conv_input(input2), 0))
#print("input 3:")
#print(pack_type(conv_input(input3), 0))
#print("input 4:")
#print(pack_type(conv_input(input4), 0))

#vsum += pack_type(conv_input(input4), vsum)
#print(pack_type(conv_input(input4), 0))
#print(vsum)

"""
def unpack(arg):
  global vsum
  if len(arg) > 10:
    version = int(arg[0:3],2)
    vsum += version
    pid = int(arg[3:6],2)
    print("version: "+str(version)+" id: "+str(pid))
    if pid == 4:
      arg = arg[6:]
      val = ""
      while True:
        val += arg[1:5]
        if arg[0] == "0":
          break
        arg = arg[5:]
      print("Literal value: "+str(int(val,2))+" arg rest: "+arg[5:])
      unpack(arg[5:])
    else:
      ltid = arg[6:7]
      print("operator: ltid: "+ltid+" arg: "+arg[7:])
      arg = arg[7:]
      if ltid == "0":
        bitlen = int(str(arg[0:15]),2)
        print("bitlen "+str(bitlen))
        vsum = unpack(arg[15:15+bitlen], vsum)
      elif ltid == "1":
        numpacks = int(str(arg[0:11]),2)
        print("numpacks "+str(numpacks))
        vsum = unpack(arg[11:], vsum, numpacks)
"""
#"""
def unpack(bit, vsum):
  if bit+11 < len(cur):
    version = int(cur[bit:bit+3],2)
    pid = int(cur[bit+3:bit+6],2)
    print("version: "+str(version)+" id: "+str(pid))
    bit += 6
    if pid == 4:
      val = ""
      while True:
        val += cur[bit+1:bit+5]
        print(cur[bit+1:bit+5])
        if cur[bit] == "0":
          break
        bit += 5
      print("Literal value: "+str(int(val,2))+" arg rest: "+cur[bit+5:])
      vsum = unpack(bit, vsum)
    else:
      ltid = cur[bit]
      print("operator: ltid: "+ltid+" arg: "+cur[bit+1:])
      if ltid == "0":
        endbit = bit+16+int(str(cur[bit+1:bit+16]),2)
        bit += 16
        while bit < endbit:
          bit, version = unpack(bit, vsum)
          vsum += version
      elif ltid == "1":
        numpacks = int(str(cur[bit+1:bit+12]),2)
        bit += 12
        for i in range(numpacks):
          bit, version = unpack(bit, vsum)
          vsum += version
    return bit, vsum


#print("input 1:") # lit 2021
#cur = conv_input(input1)
#print("vsum: "+str(unpack(0, 0)))

#print("input 2:") # op len 27 -> lit 10/20
cur = conv_input(input2)
print("vsum: "+str(unpack(0, 0)))
#"""

"""
print("input 1:")
unpack(conv_input(input1))
print("input 2:")
unpack(conv_input(input2))
print("input 3:")
unpack(conv_input(input3))
vsum=0
print("input 4:") #16 op -> op -> op -> lit
unpack(conv_input(input4))
print("vsum: "+str(vsum))

#print("input 5:") #12 op -> 2 sub -> op/op -> 2x lit
#print("vsum: "+str(unpack(conv_input(input5))))
#print("input 6:") #23 op -> 2 sub -> op/op -> 2x lit
#print("vsum: "+str(unpack(conv_input(input6))))
#print("input 7:") #31 op -> op -> op -> 5x lit
#print("vsum: "+str(unpack(conv_input(input7))))
"""