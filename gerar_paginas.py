import os

pages = [
    # Bairros e Regiões de Guarulhos (1 a 35)
    ("centro", "Centro de Guarulhos", "Atendimento expresso para comércio, clínicas e escritórios no Centro de Guarulhos."),
    ("bosque-maia", "Bosque Maia", "Motofrete rápido e seguro para a região do Bosque Maia e Av. Paulo Faccini."),
    ("vila-augusta", "Vila Augusta", "Entregas corporativas e documentos na Vila Augusta e arredores."),
    ("macedo", "Macedo", "Logística ágil e motofrete empresarial no bairro Macedo e proximidades."),
    ("gopouva", "Gopoúva", "Serviço de motoboy e transporte de malotes no Gopoúva."),
    ("vila-galvao", "Vila Galvão", "Entregas urgentes e motofrete na Vila Galvão e Zona Norte de Guarulhos."),
    ("picanco", "Picanço", "Motoboy rápido e seguro no Picanço e Av. Timóteo Penteado."),
    ("santa-mena", "Jardim Santa Mena", "Entrega expressa de documentos e contratos no Jardim Santa Mena."),
    ("cumbica", "Cumbica", "Logística e motofrete no polo industrial de Cumbica e base aérea."),
    ("bonsucesso", "Bonsucesso", "Atendimento a indústrias e galpões no Bonsucesso e região leste."),
    ("cabucu", "Cabuçu", "Serviço de motofrete e entregas na região do Cabuçu."),
    ("presidente-dutra", "Bairro Presidente Dutra", "Motoboy e distribuição rápida no bairro Presidente Dutra e margens da Dutra."),
    ("taboao", "Taboão", "Entregas corporativas e transporte de peças no Taboão."),
    ("cocaia", "Cocaia", "Logística e motofrete ágil no Cocaia."),
    ("vila-itapegica", "Vila Itapegica", "Base e atendimento imediato na Vila Itapegica e Rodovia Dutra."),
    ("paraventi", "Paraventi", "Motoboy pontual e seguro no Paraventi."),
    ("ponte-grande", "Ponte Grande", "Entregas expressas e malotes na Ponte Grande."),
    ("cecap", "Parque Residencial CECAP", "Atendimento rápido no CECAP e terminais adjacentes."),
    ("inocoop", "Inocoop", "Serviço de motofrete no Inocoop e Bonsucesso."),
    ("agua-chata", "Água Chata", "Logística B2B e transporte de cargas leves no Água Chata."),
    ("jardim-tranquilidade", "Jardim Tranquilidade", "Motoboy para comércios e residências no Jardim Tranquilidade."),
    ("vila-endres", "Vila Endres", "Entregas e malotes corporativos na Vila Endres e região do Shopping."),
    ("torres-tibagy", "Torres Tibagy", "Serviço de motofrete ágil em Torres Tibagy."),
    ("jardim-bela-vista", "Jardim Bela Vista", "Atendimento pontual no Jardim Bela Vista."),
    ("jardim-city", "Jardim City", "Motoboy expresso no Jardim City."),
    ("vila-rio", "Vila Rio", "Entregas rápidas na Vila Rio de Janeiro."),
    ("haroldo-veloso", "Haroldo Veloso", "Motofrete seguro no Haroldo Veloso."),
    ("lavras", "Lavras", "Logística e motofrete no bairro Lavras."),
    ("morros", "Morros", "Atendimento expresso na região dos Morros."),
    ("bananal", "Bananal", "Entregas corporativas no Bananal."),
    ("fortaleza", "Fortaleza", "Serviço de motoboy na Fortaleza."),
    ("mikail", "Mikail", "Motofrete rápido no Mikail."),
    ("bonsucesso-industrial", "Bonsucesso Industrial", "Logística B2B para o polo industrial do Bonsucesso."),
    ("cidade-industrial-satelite", "Cidade Industrial Satélite", "Atendimento especializado para indústrias na Cidade Industrial Satélite."),
    ("vila-rosalia", "Vila Rosália", "Motoboy e documentos na Vila Rosália e Lago dos Patos."),

    # Serviços Especializados de SEO Local (36 a 50)
    ("motoboy-urgente-guarulhos", "Motoboy Urgente em Guarulhos", "Serviço de motofrete de urgência para qualquer ponto de Guarulhos."),
    ("motoboy-empresarial-guarulhos", "Motoboy Empresarial em Guarulhos", "Contrato e atendimento dedicado para rotinas corporativas diárias."),
    ("motofrete-corporativo-guarulhos", "Motofrete Corporativo", "Soluções de transporte de pequenos volumes e documentos para empresas."),
    ("entrega-malotes-guarulhos", "Entrega de Malotes em Guarulhos", "Rotinas seguras de coleta e entrega de malotes entre matriz e filiais."),
    ("transporte-pecas-industriais-guarulhos", "Transporte de Peças Industriais", "Entrega rápida de peças (AOG) para evitar paradas em linhas de produção."),
    ("coleta-cargas-aereas-guarulhos", "Coleta de Cargas Aéreas GRU", "Retirada imediata de mercadorias despachadas via aérea no aeroporto."),
    ("entrega-documentos-cartorio-guarulhos", "Documentos em Cartórios", "Motoboy especializado em trâmites, certidões e cartórios em Guarulhos."),
    ("motoboy-24-horas-guarulhos", "Motofrete de Plantão", "Atendimento sob consulta para demandas urgentes fora do horário comercial."),
    ("logistica-b2b-guarulhos", "Logística B2B em Guarulhos", "Distribuição fracionada e atendimento logístico focado em empresas."),
    ("distribuicao-encomendas-guarulhos", "Distribuição de Encomendas", "Capilaridade e rapidez na entrega de encomendas urbanas."),
    ("motoboy-aeroporto-gru", "Motoboy no Aeroporto GRU", "Atendimento especializado nos acessos e terminais do Aeroporto de Guarulhos."),
    ("coleta-teca-aeroporto", "Coleta TECA Aeroporto", "Retirada de cargas despachadas no Terminal de Cargas."),
    ("entrega-exames-laboratoriais", "Entrega de Exames Laboratoriais", "Transporte seguro e sigiloso de exames e amostras biológicas."),
    ("motofrete-industrias-dutra", "Motofrete para Indústrias na Dutra", "Cobertura completa ao longo da Rodovia Presidente Dutra."),
    ("servico-estafeta-guarulhos", "Serviço de Estafeta Corporativo", "Profissionais dedicados para malotes, bancos e cartórios.")
]

output_dir = "/media/caas/HD_1TB/rotina-gbp-guarulhos/site-logistica-express"
os.makedirs(output_dir, exist_ok=True)

nav_links = """
<a href="index.html" class="hover:text-amber-400 transition">Início</a>
<a href="teca.html" class="hover:text-amber-400 transition">TECA GRU</a>
<a href="dutra.html" class="hover:text-amber-400 transition">Rodovia Dutra</a>
<a href="b2b.html" class="hover:text-amber-400 transition">B2B</a>
<a href="sobre.html" class="hover:text-amber-400 transition">Sobre</a>
<a href="contato.html" class="hover:text-amber-400 transition">Contato</a>
"""

for slug, title, desc in pages:
    filename = f"{slug}.html"
    filepath = os.path.join(output_dir, filename)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Motoboy e Logística Express Guarulhos</title>
    <meta name="description" content="{desc} Atendimento ágil e seguro. (11) 95724-8425.">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-900 text-slate-100 font-sans antialiased">
    <header class="bg-slate-950/80 backdrop-blur sticky top-0 z-50 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <a href="index.html" class="bg-amber-500 text-slate-950 p-2.5 rounded-xl font-black text-xl flex items-center justify-center">
                    <i class="fa-solid fa-bolt-lightning"></i>
                </a>
                <div>
                    <a href="index.html" class="block font-black text-lg tracking-wider text-white">LOGÍSTICA EXPRESS</a>
                    <span class="block text-xs text-amber-400 font-semibold uppercase tracking-widest">Guarulhos & Rodovia Dutra</span>
                </div>
            </div>
            <nav class="hidden md:flex items-center space-x-6 text-sm font-medium">
                {nav_links}
                <a href="https://wa.me/5511957248425?text=Olá,%20preciso%20de%20atendimento%20para%20{title}." target="_blank" class="bg-amber-500 text-slate-950 font-bold px-5 py-2.5 rounded-xl hover:bg-amber-400 transition flex items-center space-x-2">
                    <i class="fa-brands fa-whatsapp text-lg"></i>
                    <span>WhatsApp</span>
                </a>
            </nav>
        </div>
    </header>

    <main class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
            <div class="space-y-4 text-center">
                <div class="inline-flex items-center space-x-2 bg-amber-500/10 text-amber-400 px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider border border-amber-500/20">
                    <i class="fa-solid fa-location-dot"></i>
                    <span>Atendimento Especializado • Guarulhos</span>
                </div>
                <h1 class="text-4xl sm:text-7xl font-black tracking-tight text-white leading-tight">
                    {title}
                </h1>
                <p class="text-lg text-slate-300">
                    {desc} Contamos com profissionais treinados, motocicletas utilitárias equipadas e foco total na pontualidade corporativa.
                </p>
            </div>

            <div class="rounded-3xl overflow-hidden border border-slate-700 bg-slate-800 shadow-2xl">
                <img src="assets/hero-logistica.jpg" alt="{title}" class="w-full h-[400px] object-cover">
            </div>

            <div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-base leading-relaxed">
                <h2 class="text-2xl font-bold text-white">Por que escolher nossos serviços em {title}?</h2>
                <p>
                    A demanda por agilidade no transporte de documentos, malotes e mercadorias exige uma base logística preparada. Localizados estrategicamente na <a href="dutra.html" class="text-amber-400 underline">Rodovia Presidente Dutra (Vila Itapegica)</a>, garantimos atendimento rápido para empresas e comércios.
                </p>
                <h2 class="text-2xl font-bold text-white pt-4">Nossos Diferenciais</h2>
                <ul class="list-disc pl-6 space-y-2 text-slate-300">
                    <li>Atendimento sob demanda e rotas programadas.</li>
                    <li>Equipe uniformizada e equipada conforme a Lei 12.009/09.</li>
                    <li>Integração direta com coletas no <a href="teca.html" class="text-amber-400 underline">TECA GRU</a> e aeroporto.</li>
                    <li>Foco em soluções <a href="b2b.html" class="text-amber-400 underline">B2B e indústrias</a>.</li>
                </ul>
            </div>

            <div class="bg-slate-950 p-8 sm:p-10 rounded-3xl border border-slate-800 text-center space-y-6">
                <h3 class="text-2xl font-bold text-white">Precisa de Atendimento Imediato?</h3>
                <p class="text-slate-400 text-sm">Fale diretamente com nossa central pelo WhatsApp e solicite seu orçamento.</p>
                <a href="https://wa.me/5511957248425?text=Olá,%20preciso%20de%20atendimento%20para%20{title}." target="_blank" class="inline-flex items-center space-x-3 bg-amber-500 text-slate-950 font-extrabold px-8 py-4 rounded-2xl hover:bg-amber-400 transition shadow-lg text-base">
                    <i class="fa-brands fa-whatsapp text-2xl"></i>
                    <span>Chamar no WhatsApp (11) 95724-8425</span>
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-slate-950 py-12 border-t border-slate-900 text-center text-xs text-slate-500 space-y-4">
        <div class="flex flex-wrap justify-center gap-4 pb-4 font-medium text-slate-400">
            <a href="index.html" class="hover:text-amber-400">Início</a>
            <a href="teca.html" class="hover:text-amber-400">TECA GRU</a>
            <a href="dutra.html" class="hover:text-amber-400">Rodovia Dutra</a>
            <a href="b2b.html" class="hover:text-amber-400">B2B</a>
            <a href="sobre.html" class="hover:text-amber-400">Sobre</a>
            <a href="contato.html" class="hover:text-amber-400">Contato</a>
        </div>
        <p>© 2026 Motoboy e Logística Express. Todos os direitos reservados.</p>
        <p>Rod. Pres. Dutra - Pista Lateral, 225 - Vila Itapegica, Guarulhos - SP • WhatsApp: (11) 95724-8425</p>
    </footer>
</body>
</html>
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("50 páginas geradas com sucesso!")
