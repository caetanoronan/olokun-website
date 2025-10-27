# 🌊 Olokun - Gestão Ambiental Inteligente

Site moderno e tecnológico para a startup Olokun, especializada em gestão de resíduos sólidos e sustentabilidade empresarial.

## 📋 Sobre o Projeto

A Olokun oferece soluções completas para gestão ambiental empresarial, transformando desafios ambientais em oportunidades de negócio.

## 🚀 Tecnologias Utilizadas

### Frontend
- **HTML5** - Estrutura semântica moderna
- **CSS3** - Design system completo com variáveis CSS
- **JavaScript ES6+** - Interatividade e animações
- **AOS (Animate On Scroll)** - Animações suaves ao rolar
- **Font Awesome** - Ícones profissionais
- **Google Fonts (Inter)** - Tipografia moderna

### Design & UX
- **Design Responsivo** - Funciona em todos os dispositivos
- **Mobile First** - Otimizado para dispositivos móveis
- **Gradientes Modernos** - Visual tecnológico e atrativo
- **Microinterações** - Feedback visual em tempo real
- **Acessibilidade** - Suporte a leitores de tela e navegação por teclado

## 📁 Estrutura do Projeto

```
Olokun/
├── index.html              # Página principal
├── pgrs.html              # Página PGRS Inteligente
├── capacitacao.html       # Página Capacitação
├── consultoria.html       # Página Consultoria Estratégica
├── styles.css             # Estilos principais
├── script.js              # JavaScript principal
└── README.md              # Documentação
```

## 🎨 Design System

### Cores Principais
- **Primário**: `#2563eb` (Azul profissional)
- **Secundário**: `#10b981` (Verde sustentabilidade)
- **Accent**: `#f59e0b` (Dourado premium)
- **Gradientes**: Combinações modernas para visual impactante

### Tipografia
- **Família**: Inter (Google Fonts)
- **Pesos**: 300, 400, 500, 600, 700, 800
- **Hierarquia**: Sistema de tamanhos responsivos

### Componentes
- **Buttons**: 3 variações com efeitos hover
- **Cards**: Elevação e animações
- **Forms**: Validação em tempo real
- **Navigation**: Menu responsivo com animações

## 📱 Páginas do Site

### 1. Página Principal (index.html)
- **Hero Section**: Apresentação impactante da empresa
- **Serviços**: Cards interativos dos principais serviços
- **Sobre**: História e diferenciais da Olokun
- **Benefícios**: Vantagens para clientes
- **CTA**: Chamadas para ação estratégicas
- **Contato**: Formulário otimizado para conversão

### 2. PGRS Inteligente (pgrs.html)
- **Processo**: Timeline visual da metodologia
- **Compliance**: Requisitos legais e benefícios
- **Conteúdo**: Detalhamento do documento técnico
- **Investimento**: Transparência nos preços
- **Formulário**: Específico para PGRS

### 3. Capacitação (capacitacao.html)
- **Módulos**: 6 módulos especializados detalhados
- **Metodologia**: Abordagem prática e teórica
- **Investimento**: Tabela comparativa de pacotes
- **Depoimentos**: Casos de sucesso
- **Formulário**: Inscrições para treinamentos

### 4. Consultoria Estratégica (consultoria.html)
- **Estratégia**: Matriz de alinhamento estratégico
- **ROI**: Calculadora de retorno de investimento
- **Processo**: 4 fases da consultoria
- **Case Study**: Caso real de sucesso
- **Formulário**: Solicitação personalizada

## 🔧 Funcionalidades

### JavaScript Avançado
- **Navegação Inteligente**: Menu que se adapta ao scroll
- **Animações**: AOS e animações CSS customizadas
- **Formulários**: Validação em tempo real e envio
- **Performance**: Lazy loading e otimizações
- **Acessibilidade**: Suporte completo a navegação por teclado

### Formulários Inteligentes
- **Validação**: HTML5 + JavaScript personalizado
- **UX**: Feedback visual em tempo real
- **Integração**: Mailto customizado para cada serviço
- **Conversão**: Otimizados para geração de leads

### Responsividade
- **Breakpoints**: Mobile, Tablet, Desktop
- **Imagens**: Responsivas e otimizadas
- **Tipografia**: Escalas fluidas
- **Layout**: Grid CSS moderno

## 🚀 Como Usar

### 1. Configuração Local
```bash
# Clone o repositório ou baixe os arquivos
# Abra index.html em qualquer navegador moderno
# Não requer servidor - funciona como arquivos estáticos
```

### 2. Hospedagem
- **GitHub Pages**: Hospedagem gratuita
- **Netlify**: Deploy automático
- **Vercel**: Otimizações automáticas
- **Hosting tradicional**: Qualquer servidor web

### 3. Customização
- **Cores**: Altere as variáveis CSS em `:root`
- **Conteúdo**: Edite os textos diretamente no HTML
- **Imagens**: Substitua os placeholders por imagens reais
- **Formulários**: Configure integração com seu sistema

## 📧 Configuração de Formulários

Os formulários estão configurados para usar `mailto:` por padrão. Para produção, recomenda-se integrar com:

### Opções Recomendadas
- **Formspree**: Formulários sem backend
- **Netlify Forms**: Integração nativa
- **EmailJS**: Envio direto do frontend
- **API própria**: Backend personalizado

### Exemplo de Integração
```javascript
// Substituir o mailto por API
async function submitForm(data) {
    const response = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return response.json();
}
```

## 🔍 SEO e Performance

### Meta Tags
- **Title**: Títulos otimizados por página
- **Description**: Descrições únicas e atrativas
- **Viewport**: Configuração mobile-first
- **Charset**: UTF-8 para caracteres especiais

### Performance
- **CSS**: Minificação recomendada para produção
- **JavaScript**: Carregamento assíncrono
- **Fontes**: Preload e preconnect configurados
- **Imagens**: Lazy loading implementado

### Analytics
Adicione seu código de Google Analytics:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🛠️ Manutenção

### Atualizações Regulares
- **Conteúdo**: Manter informações atualizadas
- **Preços**: Revisar tabelas de investimento
- **Depoimentos**: Adicionar novos casos de sucesso
- **Blog**: Adicionar seção de artigos (futuro)

### Monitoramento
- **Analytics**: Acompanhar métricas de conversão
- **Formulários**: Monitorar taxa de preenchimento
- **Performance**: PageSpeed Insights regular
- **Acessibilidade**: Testes com ferramentas WAVE

## 🎯 Objetivos de Negócio

### Conversão
- **Leads**: Formulários otimizados por serviço
- **Credibilidade**: Design profissional e moderno
- **Confiança**: Cases e depoimentos reais
- **Autoridade**: Conteúdo técnico especializado

### Marketing
- **SEO**: Estrutura otimizada para buscadores
- **Social**: Compartilhamento facilitado
- **Mobile**: Experiência perfeita em dispositivos móveis
- **Speed**: Carregamento rápido para melhor UX

## 📞 Contato e Suporte

### Informações da Empresa
- **Email**: olokun.ambiental@gmail.com
- **Website**: https://olokun.webnode.com/
- **Localização**: Florianópolis, SC - Brasil

### Desenvolvimento
- **Criado em**: Janeiro 2025
- **Tecnologia**: HTML5, CSS3, JavaScript
- **Status**: Produção
- **Última atualização**: Janeiro 2025

---

## 📄 Licença

Projeto desenvolvido para Olokun Gestão Ambiental. Todos os direitos reservados.

---

*"Transformando desafios ambientais em oportunidades de negócio."* 🌊