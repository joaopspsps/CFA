# webREPL

Acho que concluí uma história, agora vou contar...

Na animação abaixo o Witty Board está conectado por wifi à minha rede doméstica, tal como o computador que estou usando. Eles estão a uns dois metros de distância um do outro e não estão interconectados por cabos de comunicação (ex. USB - o cabo USB conectado ao witty board está conectado a uma fonte de alimentação). Consigo acender e apagar o LED através da conexão WiFi.

![webREPL em ação](./output.gif)

### O que é webREPL

webREPL é uma ferramenta que permite usar um navegador web para enviar comandos Python através da conexão de rede para um dispositivo (ex. Witty Board).

A fim de entender o funcionamento e explicar a implantação da ferramenta, assume-se que esta tem duas partes. Uma parte, "C", é executada no computador e outra, "D", é executada no dispositivo. "D" consiste em módulos do Python, requer algumas configurações E uma conexão WiFi ativa. "C" consiste em uma página html e scripts JavaScript.

A conexão WiFi é ativada por estes comandos:

```python
import network, time
staif=network.WLAN(network.STA_IF) 
staif.connect('SSID', 'PASSWORD') # preenche se quiser mudar
staif.active(True) # conecta ao ap conectado anteriormente
time.sleep(5)
staif.isconnected() # True se conectou
staif.ifconfig()    # Mostra o IP para conexão da parte "C"
```
Referência: https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html, 

O módulo webREPL é configurado com o comando abaixo e respondendo para habilitar o webrepl e entrar com um password:

```
import webrepl_setup

```
Referência: https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl, https://www.srccodes.com/setup-web-repl-esp8266-12e-connect-micro-python-prompt-repl-wifi-access-point-ap-hello-world/

Após estes passos, o dispositivo está pronto para receber comandos pelo WiFi, o que conclui a parte "D", mas, se o dispositivo for reiniciado ou se a energia desligar e retornar, a conexão WiFi precisará ser (novamente) ativada. É mais fácil fazer isso usando webREPL por isso adia-se o passo de tornar a conexão permanente.

A parte "C" consiste em clonar o repositório https://github.com/micropython/webrepl e abrir `webrepl.html` no navegador. Uma página com aparência semelhante à apresentada na figura abaixo deve ser mostrada.

![webREPL e boot.py](./Captura2022-07-13-22-37-39.png)

Para conectar, substituir o IP na caixa de texto ao lado do botão Connect pelo IP apresentado pelo dispositivo durante a configuração do wifi. Manter o `:8266`. Clicar em Connect, digitar a senha usada na execução de `webrepl_setup`, deve aparecer a mensagem WebREPL Connected e o prompt (>>>).


### Tornar a conexão permanente.

Para tornar a conexão permanente, acrescentar a ativação da rede no arquivo `boot.py`. 

Nesta pasta há uma cópia do `boot.py` resultante desse acréscimo. Caso este sirva, usando webREPL, renomeie o `boot.py` original usando o comando `os.rename()` (https://docs.micropython.org/en/v1.7/esp8266/library/os.html), depois, transfira o novo `boot.py` para o dispositivo usando o botão `Send a file`.


### Comandos usados para gravar vídeo e converter em gif animado:

```
recordmydesktop --fps=15 --no-sound --v_quality=32
ffmpeg -i out.ogv -s 640x480 -r 7 -filter:v "setpts=PTS/3" -ss 00:00:01 -t 00:00:16.5 output.gif
```

Referência sobre como acelerar o vídeo: https://superuser.com/questions/1261678/how-do-i-speed-up-a-video-by-60x-in-ffmpeg

Referência com módulos para micropython: https://awesome-micropython.com/

mDNS facilitaria o uso de WebREPL, mas parece que não há implementação de mDNS para ESP8266...

- https://github.com/cbrand/micropython-mdns
- https://github.com/micropython/micropython/issues/2875
- https://github.com/micropython/micropython/issues/4912
- https://community.hiveeyes.org/t/esp32-network-discovery-through-mdns-with-micropython/2253
