<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
.s3 { color: #6897bb;}
.ln { color: #606366; font-weight: normal; font-style: normal; }
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><a name="l1"><span class="ln">1    </span></a><span class="s0">print(</span><span class="s1">&quot;Cadastre aqui sua senha com os seguintes criétios: </span><span class="s2">\n</span><span class="s1">&quot;</span>
<a name="l2"><span class="ln">2    </span></a>      <span class="s1">&quot;         *Ao menos 6 digitos</span><span class="s2">\n</span><span class="s1">&quot;</span>
<a name="l3"><span class="ln">3    </span></a>      <span class="s1">&quot;         *Ao menos uma letra MAIÚSCULA</span><span class="s2">\n</span><span class="s1">&quot;</span>
<a name="l4"><span class="ln">4    </span></a>      <span class="s1">&quot;         *Ao menos um número</span><span class="s2">\n</span><span class="s1">&quot;</span>
<a name="l5"><span class="ln">5    </span></a>      <span class="s1">&quot;         *Ao menos um caractere especial(!@#$%¨&amp;*)</span><span class="s2">\n</span><span class="s1">&quot;</span><span class="s0">)</span>
<a name="l6"><span class="ln">6    </span></a><span class="s2">while True</span><span class="s0">:</span>
<a name="l7"><span class="ln">7    </span></a>    <span class="s0">senha = str(input(</span><span class="s1">&quot;Digite sua senha : &quot;</span><span class="s0">))</span>
<a name="l8"><span class="ln">8    </span></a>    <span class="s2">if </span><span class="s0">senha.islower():</span>
<a name="l9"><span class="ln">9    </span></a>        <span class="s0">print(</span><span class="s1">&quot;A senha deve ter pelo menos um caractere MAIUSCULO: &quot;</span><span class="s0">)</span>
<a name="l10"><span class="ln">10   </span></a>    <span class="s2">elif </span><span class="s0">len(senha) &lt; </span><span class="s3">5</span><span class="s0">:</span>
<a name="l11"><span class="ln">11   </span></a>        <span class="s0">print(</span><span class="s1">&quot;A senha deve ter pelo menos 6 caracteres: &quot;</span><span class="s0">)</span>
<a name="l12"><span class="ln">12   </span></a>    <span class="s2">elif </span><span class="s0">senha.isupper():</span>
<a name="l13"><span class="ln">13   </span></a>        <span class="s0">print(</span><span class="s1">&quot;A senha deve ter pelo menos um caractere Minusculo: &quot;</span><span class="s0">)</span>
<a name="l14"><span class="ln">14   </span></a>    <span class="s2">elif </span><span class="s0">senha.isalpha():</span>
<a name="l15"><span class="ln">15   </span></a>        <span class="s0">print(</span><span class="s1">&quot;Necessita de um numero: &quot;</span><span class="s0">)</span>
<a name="l16"><span class="ln">16   </span></a>    <span class="s2">elif </span><span class="s0">senha.isalnum():</span>
<a name="l17"><span class="ln">17   </span></a>        <span class="s0">print(</span><span class="s1">&quot;Necessita de um Caractere especial: &quot;</span><span class="s0">)</span>
<a name="l18"><span class="ln">18   </span></a>    <span class="s2">else</span><span class="s0">:</span>
<a name="l19"><span class="ln">19   </span></a>        <span class="s2">break</span></pre>
</body>
</html>