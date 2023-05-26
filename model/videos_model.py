from model.entity.video import Video


class Videos_model:
    def __init__(self):

        a_ilha_misteriosa = Video(0,"https://www.youtube.com/embed/e5m5g9mY204", "viagem2.jfif","A ILHA MISTERIOSA", "Sean Anderson descobre uma misteriosa mensagem de rádio, que ele acredita tenha sido enviada por seu avô desaparecido há dois anos. Ele não gosta muito de seu padrasto Hank Parsons, mas o cara consegue ajudá-lo a decifrar os códigos do texto e juntos eles descobrem o paradeiro do coroa aventureiro numa ilha misteriosa, difundida pelo escritor Julio Verne, entre outros. Para chegar lá, a dupla contrata o piloto de helicóptero Gabato e sua filha Kailani, mas muitos perigos aguardam os viajantes e sobreviver implicará numa série de incríveis aventuras.", 10,10,"13/05/2004",0)
        a_pequena_sereia = Video(1,"https://www.youtube.com/embed/G64vg5OUDOs", "a-pequena-sereia.jpg","A Pequena Sereia (2018)", "Um jovem repórter vai fazer uma reportagem sobre um circo que diz apresentar uma sereia de verdade. Inicialmente cético, ele leva sua jovem sobrinha na viagem e lá eles descobrem uma bela e encantadora criatura a qual eles acreditam ser realmente uma sereia. Juntos eles embarcam numa aventura para salvar a vida da moça naquele lugar.", 9,9,"10/01/2021",0)
        o_mundo_novo = Video(2,"https://www.youtube.com/embed/EgSVwHr0P1I", "um-mundo-novo.jfif","Um Mundo Novo", "Matt, um jornalista, e sua noiva são mortos em uma explosão. Eles então acordam em um planeta que mantém as almas de todos aqueles que um dia já passaram pela Terra.", 10,10,"13/05/2004",1)
        viagem_ao_vale = Video(3,"https://www.youtube.com/embed/PJoGVv8INc4", "viagem-ao-vale.jpg","VIAGEM AO VALE PROIBIDO", "Depois que seu avião cai na floresta da China central, um menino e seu guardião encontram um homem-macaco indescritível conhecido como yeren.", 9,9,"10/01/2021",1)
        olhos_famintos_4 = Video(4,"https://www.youtube.com/embed/1BytyoMyqOc", "olhos-famintos.jfif","OLHOS FAMINTOS 4 O RENASCIMENTO", "A caminho de um festival de terror, Laine começa a ter visões perturbadoras sobre o passado do lugar onde está indo. A celebração rapidamente se transforma em um banho de sangue, e uma presença maligna parece ter sido despertada.", 10,10,"13/05/2004",2)
        o_arrebatamento = Video(5,"https://www.youtube.com/embed/nQnWsiKNLWI" , "o-arrebatamento.jfif","Filme O Arrebatamento o Juízo Final", "Filme O Arrebatamento o Juízo Final, Dublado e Completo em Português 2023", 9,9,"10/01/2021",2)

        todosVideos = [a_ilha_misteriosa,a_pequena_sereia,o_mundo_novo,viagem_ao_vale,olhos_famintos_4,o_arrebatamento]
        self.todosVideos = todosVideos
        

    def EsteVideo(self,id):
        videoCerto=[]

        for esteVideo in self.todosVideos:
            if esteVideo.id == int(id):
                videoCerto.append(esteVideo) 

        return videoCerto
    
    def VideosDestaCategoria(self,id):
        
        videos= []

        for videosDaCategoria in self.todosVideos:
            if videosDaCategoria.categoria == int(id):
                videos.append(videosDaCategoria)
        
        return videos
           

    

