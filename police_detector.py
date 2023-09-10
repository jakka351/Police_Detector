#coding:utf-8
#################################################################################################################
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################################################
# Utility to detect Victoria Police officers within bluetooth signal range via their body worn camera.
#################################################################################################################
'''
                                                                                                         
 *#####:         .##:*##                   @@@@@: @@@@@@=#@@@@@@#-@@@@@@  @@@@@:@@@@@@@= @@@@@@ -@@@@@   
 #######-        .##:###                   @@@@@- @@@@@@=#@@@@@@#-@@@@@@ .@@@@@:@@@@@@@= @@@@@@ -@@@@@   
 ###::###  -==:  .##:-=-   ===     ===     @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###  ### ###### .##:###  #####- .#####:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@=  @@  
 #######*-##. ##:.##:### *## ### ##+ :##   @%  %@ @@@@%     @@   -@@@@.  @@        @@   %@    @#-@@@@@   
 ######* +##  ##*.##:### ###     #######.  @%  %@ @@@@*     @@   -@@@@   @@        @@   %@    @#-@@@@@.  
 ###     =##  ##*.##:### ### :** ##+  .:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###      ###### .##:### -#####* =##*##*   @@--@# @@----.   @@   -@*---- *@----    @@   =@=--=@=-@-  @@  
 *##      .####. .##.*##  -###+   -###+    @@@@@: @@@@@@+   @@   -@@@@@@  @@@@@:   @@    @@@@@@ -@-  @@  
                                           =====. ======:   ==   .======  =====    =-    ====== .=.  ==  

"If He Was Going To Commit A Crime, Would He Have Invited The Number One Cop In Town? Now, Where Did I Put My Gun?
Oh Yeah, I Set It Down When I Got A Piece Of Cake!" - Clancy Wiggum, Chief of Victoria Police. 
'''
#################################################################################################################
# Open Sauce Software, tasty and free!
#################################################################################################################
import simplepyble, time, threading, logging
#################################################################################################################

def logo():
    print(
            '''
#################################################################################################################
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################################################
# Utility to detect Victoria Police officers within bluetooth signal range via their body worn camera.
#################################################################################################################

                                                                                                         
 *#####:         .##:*##                   @@@@@: @@@@@@=#@@@@@@#-@@@@@@  @@@@@:@@@@@@@= @@@@@@ -@@@@@   
 #######-        .##:###                   @@@@@- @@@@@@=#@@@@@@#-@@@@@@ .@@@@@:@@@@@@@= @@@@@@ -@@@@@   
 ###::###  -==:  .##:-=-   ===     ===     @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###  ### ###### .##:###  #####- .#####:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@=  @@  
 #######*-##. ##:.##:### *## ### ##+ :##   @%  %@ @@@@%     @@   -@@@@.  @@        @@   %@    @#-@@@@@   
 ######* +##  ##*.##:### ###     #######.  @%  %@ @@@@*     @@   -@@@@   @@        @@   %@    @#-@@@@@.  
 ###     =##  ##*.##:### ### :** ##+  .:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###      ###### .##:### -#####* =##*##*   @@--@# @@----.   @@   -@*---- *@----    @@   =@=--=@=-@-  @@  
 *##      .####. .##.*##  -###+   -###+    @@@@@: @@@@@@+   @@   -@@@@@@  @@@@@:   @@    @@@@@@ -@-  @@  
                                           =====. ======:   ==   .======  =====    =-    ====== .=.  ==  

"If He Was Going To Commit A Crime, Would He Have Invited The Number One Cop In Town? Now, Where Did I Put My Gun?
Oh Yeah, I Set It Down When I Got A Piece Of Cake!" - Clancy Wiggum, Chief of Victoria Police. 

#################################################################################################################
# Open Sauce Software, tasty and free!
#################################################################################################################
                                            '''
        )


#if __name__ == "__main__":
def GetBluetoothMacList():
    global count
    adapters = simplepyble.Adapter.get_adapters()

    if len(adapters) == 0:
        print("No adapters found")

    # Query the user to pick an adapter
    #print("Please select an adapter:")
    #for i, adapter in enumerate(adapters):
    #    print(f"{i}: {adapter.identifier()} [{adapter.address()}]")

    choice = int(0)
    adapter = adapters[choice]

    print(f"Selected adapter: {adapter.identifier()} [{adapter.address()}]")

    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    adapter.set_callback_on_scan_found(lambda peripheral: print(f"Found {peripheral.identifier()} [{peripheral.address()}]"))

    # Scan for 5 seconds
    adapter.scan_for(5000)

    peripherals = adapter.scan_get_results()
    count = count + 1
    print("Scan Count:", count)
    addr = "00:25:DF"
    for peripheral in peripherals:
        #print(peripheral.address())
        if "00:25:DF" in peripheral.address():
            #print("POLICE in proximity")
            print(
            '''
#################################################################################################################                                                                                                         

 *#####:         .##:*##                                      [ DETECTED IN PROXIMITY ]
 #######-        .##:###                                      [ DETECTED IN PROXIMITY ]
 ###::###  -==:  .##:-=-   ===     ===                        [ DETECTED IN PROXIMITY ]
 ###  ### ###### .##:###  #####- .#####:                      [ DETECTED IN PROXIMITY ]
 #######*-##. ##:.##:### *## ### ##+ :##                      [ DETECTED IN PROXIMITY ]
 ######* +##  ##*.##:### ###     #######.                     [ DETECTED IN PROXIMITY ]
 ###     =##  ##*.##:### ### :** ##+  .:                      [ DETECTED IN PROXIMITY ]
 ###      ###### .##:### -#####* =##*##*                      [ DETECTED IN PROXIMITY ]
 *##      .####. .##.*##  -###+   -###+                       [ DETECTED IN PROXIMITY ]

#################################################################################################################
                                            '''
        )
        else:
            print("No Police Detected")
def detect():
    while True:
        try:
            #logo()
            GetBluetoothMacList()
        except:
            break

if __name__ == "__main__":
    count = 0
    x = threading.Thread(target=detect)
    x.start()
    # x.join()
