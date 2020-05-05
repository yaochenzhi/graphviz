[ install ]
    [ bin ]
        [ linux ]
            yum install -y php php-json

            curl -O https://getcomposer.org/installer

            php installer

            composer.phar require graphp/graphviz
        
        [ windows ]
            https://graphviz.gitlab.io/download/
    
    [ pip ]
        # https://graphviz.readthedocs.io/en/stable/manual.html#installation
        pip install graphviz    

[ output ]
    [ render ]
        graphviz.Digraph().render('/dst/path/to/file', view=True)

    [ jupter ]
        graphviz.Digraph()