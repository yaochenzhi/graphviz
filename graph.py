from graphviz import Digraph
import os


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


dot = Digraph(comment='The Round Table')

dot.node('dns server', 'dns server')
dot.node('dns protocol', 'dns protocol')
dot.node('dnscrypt-proxy', 'dnscrypt-proxy')
dot.node('doh-server', 'doh-server (bind ip:port)')
dot.node('doh-client', 'doh-client')

dot.node('web', 'web-server(bind domain)')
dot.node('cloudflared', 'cloudflared')
dot.node('localhost', 'localhost')


dot.edge('dns server', 'dnscrypt-proxy')
dot.edge('dns protocol', 'doh-server')
dot.edge('dns server', 'dns protocol', color='orange')
dot.edge('dnscrypt-proxy', 'dns protocol', color='orange')
dot.edge('doh-server', 'doh-client')
dot.edge('doh-client', 'dns protocol', color='orange')
dot.edge('dns protocol', 'localhost', color='green')
dot.edge('doh-server', 'web')
dot.edge('web', 'cloudflared')
dot.edge('web', 'doh-client', color='pink')     # cloudflare has already provide the public
dot.edge('cloudflared', 'dns protocol', color='orange')
dot.render('graph.png', view=True)