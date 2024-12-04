Aluno: Davi Camargo


1.
A principal diferença entre os dois, é que o Selenium IDE é de certa forma mais simples, não envolve programação e é uma extensão para os navegadores. Enquanto isso, o Selenium webdriver é uma biblioteca que permite a criação de automatizações através de diversas linguagens de programação.



2.
element = driver.find_element(By.xx, “xxxx”)

Os principais são: ID, Name, Class name, Xpath, Tag_Name..

O localizador “ID” é usado pra encontrar elementos pelo ID único desse elemento html.
<input type="text" id="username" />

O Xpath Usa uma linguagem que permite a navegação na estrutura DOM do HTML.. Permitindo localizar elementos com base em sua hierarquia posição ou atributos.



3.
WebElement é basicamente um elemento único da página, como um botão por exemplo. Permite interação com esse elemento..



4.
Caso isso ocorra, o python vai simplesmente retornar exceções, pode ser o NoSuchElementException ou outros..
Uma maneira simples e eficaz de evitar com que isso ocorra, é adicionando um wait(1) entre as ações.



5.
No geral, o simples fato de o Selenium IDE não ser programável já é uma grande limitação quando comparado com o Webdriver, um dos motivos é a falta de opções ao se deparar com um evento arbitrário como aparições de um pop-up. Também pode-se observar que o Selenium webdriver pode tirar print da tela ou até mesmo criar documentos.
