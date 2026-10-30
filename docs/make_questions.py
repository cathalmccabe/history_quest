import json
# Category | event | date YYYY-MM-DD or YYYY | context
raw='''Ancient & Medieval|Traditional founding of Rome|753 BCE|Traditional Roman dating places the founding of Rome in 753 BCE.
Ancient & Medieval|Julius Caesar assassinated|44 BCE-03-15|Caesar was killed on the Ides of March.
Ancient & Medieval|Roman invasion of Britain begins|43|Roman forces invaded Britain under Emperor Claudius.
Ancient & Medieval|Western Roman Empire traditionally ends|476|Romulus Augustulus was deposed in 476.
Ancient & Medieval|Battle of Clontarf|1014-04-23|Brian Boru's forces fought at Clontarf on Good Friday.
Ancient & Medieval|Battle of Hastings|1066-10-14|William of Normandy defeated King Harold II.
Ancient & Medieval|Norman invasion of Ireland begins|1169|Anglo-Norman forces arrived in Ireland in 1169.
Ancient & Medieval|Magna Carta sealed|1215-06-15|King John agreed to Magna Carta at Runnymede.
Ancient & Medieval|Black Death reaches Ireland|1348|The plague reached Ireland in 1348.
Renaissance & Reformation|Gutenberg Bible completed approximately|1455|Gutenberg's printed Bible dates to around 1455.
Renaissance & Reformation|Columbus reaches the Caribbean|1492-10-12|Columbus landed in the Caribbean in October 1492.
Renaissance & Reformation|Vasco da Gama reaches India by sea|1498|The Portuguese expedition reached Calicut in 1498.
Renaissance & Reformation|Martin Luther's Ninety-five Theses|1517|The Ninety-five Theses are traditionally dated to 1517.
Renaissance & Reformation|Henry VIII becomes King of England|1509|Henry VIII began his reign in 1509.
Renaissance & Reformation|Act of Supremacy in England|1534|The Act established Henry VIII as supreme head of the Church of England.
Renaissance & Reformation|Dissolution of the monasteries begins|1536|Henry VIII's dissolution programme began in 1536.
Renaissance & Reformation|Council of Trent begins|1545|The Catholic council opened in 1545.
Renaissance & Reformation|Elizabeth I becomes Queen of England|1558|Elizabeth I began her reign in 1558.
Renaissance & Reformation|Spanish Armada defeated|1588|The Spanish Armada campaign took place in 1588.
Early Modern Ireland|Nine Years' War begins in Ireland|1594|The conflict is commonly dated from 1594 to 1603.
Early Modern Ireland|Battle of Kinsale|1601|Irish and Spanish forces were defeated at Kinsale.
Early Modern Ireland|Flight of the Earls|1607|Hugh O'Neill and Rory O'Donnell left Ireland in 1607.
Early Modern Ireland|Plantation of Ulster begins|1609|The organised plantation programme began in 1609.
Early Modern Ireland|Irish Rebellion of 1641|1641|Rebellion broke out in Ireland in October 1641.
Early Modern Ireland|Cromwell's siege of Drogheda|1649|Cromwell's forces captured Drogheda in 1649.
Early Modern Ireland|Battle of the Boyne|1690-07-01|The battle was fought on 1 July Old Style, 11 July New Style. This card uses Old Style.
Early Modern Ireland|Treaty of Limerick|1691|The treaty was signed after the Williamite War.
Early Modern Ireland|Penal Laws intensified in Ireland|1695|Important penal legislation was passed in 1695.
Revolutions|American Declaration of Independence|1776-07-04|The Declaration was adopted on 4 July 1776.
Revolutions|US Constitution signed|1787-09-17|Delegates signed the Constitution in Philadelphia.
Revolutions|Storming of the Bastille|1789-07-14|The storming became a symbol of the French Revolution.
Revolutions|French Revolution begins|1789|The Revolution began in 1789.
Revolutions|Louis XVI executed|1793-01-21|The French king was executed in Paris.
Revolutions|Napoleon becomes Emperor of the French|1804|Napoleon was crowned emperor in 1804.
Revolutions|Battle of Waterloo|1815-06-18|Napoleon was defeated at Waterloo.
Revolutions|Haitian independence declared|1804-01-01|Haiti declared independence from France.
Industrial & 19th Century|James Watt patents improved steam engine|1769|Watt patented a separate condenser design.
Industrial & 19th Century|First passenger railway opens between Stockton and Darlington|1825|The Stockton and Darlington Railway opened in 1825.
Industrial & 19th Century|Liverpool and Manchester Railway opens|1830|An early intercity passenger railway opened in 1830.
Industrial & 19th Century|Great Exhibition in London|1851|The Great Exhibition was held at the Crystal Palace.
Industrial & 19th Century|Charles Darwin publishes On the Origin of Species|1859|Darwin's major work was published in 1859.
Industrial & 19th Century|German unification proclaimed|1871|The German Empire was proclaimed in Versailles.
Industrial & 19th Century|Alexander Graham Bell patents telephone|1876|Bell received a US patent for the telephone in 1876.
Industrial & 19th Century|First modern Olympic Games|1896|The first modern Olympics were held in Athens.
Ireland 1798–1914|United Irishmen rebellion|1798|The rebellion took place across Ireland in 1798.
Ireland 1798–1914|Act of Union takes effect|1801-01-01|The Kingdom of Great Britain and Ireland came into being.
Ireland 1798–1914|Catholic Emancipation|1829|The Roman Catholic Relief Act was passed in 1829.
Ireland 1798–1914|Great Famine begins|1845|Potato blight struck in 1845.
Ireland 1798–1914|Great Famine commonly considered to end|1852|The Great Famine is usually dated 1845–1852.
Ireland 1798–1914|Young Ireland rebellion|1848|The Young Ireland rising took place in 1848.
Ireland 1798–1914|Irish National Land League founded|1879|The Land League was founded in 1879.
Ireland 1798–1914|First Home Rule Bill introduced|1886|Gladstone introduced the first Home Rule Bill.
Ireland 1798–1914|Gaelic Athletic Association founded|1884|The GAA was founded in Thurles in 1884.
Ireland 1798–1914|Gaelic League founded|1893|Conradh na Gaeilge was founded in 1893.
Ireland 1798–1914|Dublin Lockout begins|1913|The major industrial dispute began in 1913.
Ireland 1798–1914|Irish Volunteers founded|1913|The Irish Volunteers were founded in November 1913.
Ireland 1916–1923|Easter Rising begins|1916-04-24|The Rising began on Easter Monday.
Ireland 1916–1923|Easter Rising ends with surrender|1916-04-29|Patrick Pearse ordered surrender on 29 April.
Ireland 1916–1923|Proclamation of the Irish Republic read|1916-04-24|The Proclamation was read outside the GPO.
Ireland 1916–1923|Sinn Féin general election victory|1918|Sinn Féin won most Irish seats in the 1918 UK election.
Ireland 1916–1923|First Dáil meets|1919-01-21|The First Dáil met in Dublin.
Ireland 1916–1923|Irish War of Independence begins|1919|The conflict is generally dated 1919–1921.
Ireland 1916–1923|Bloody Sunday in Dublin|1920-11-21|Killings occurred in Dublin on 21 November 1920.
Ireland 1916–1923|Truce in Irish War of Independence|1921-07-11|The truce began on 11 July 1921.
Ireland 1916–1923|Anglo-Irish Treaty signed|1921-12-06|The Treaty was signed in London.
Ireland 1916–1923|Irish Civil War begins|1922-06-28|Fighting began at the Four Courts.
Ireland 1916–1923|Irish Free State established|1922-12-06|The Irish Free State came into being.
Ireland 1916–1923|Irish Civil War ends|1923|The anti-Treaty IRA ordered an end to its campaign in 1923.
World War I|Archduke Franz Ferdinand assassinated|1914-06-28|The assassination in Sarajevo helped trigger World War I.
World War I|World War I begins|1914|The war began in Europe in 1914.
World War I|Germany invades Belgium|1914-08-04|Germany's invasion brought Britain into the war.
World War I|Battle of the Somme begins|1916-07-01|The Somme offensive began on 1 July 1916.
World War I|Battle of Verdun begins|1916-02-21|The battle began in February 1916.
World War I|United States enters World War I|1917-04-06|The United States declared war on Germany.
World War I|Russian Revolution|1917|Russia experienced major revolutions in 1917.
World War I|Armistice ends fighting on Western Front|1918-11-11|The armistice took effect at 11 a.m.
World War I|Treaty of Versailles signed|1919-06-28|The peace treaty was signed in 1919.
World War II|Hitler becomes German chancellor|1933-01-30|Hitler was appointed chancellor of Germany.
World War II|Nuremberg Laws introduced|1935|The Nazis enacted antisemitic racial laws in 1935.
World War II|Kristallnacht|1938-11-09|The Nazi pogrom began on the night of 9 November.
World War II|Germany invades Poland|1939-09-01|The invasion began World War II in Europe.
World War II|Britain and France declare war on Germany|1939-09-03|Both countries declared war after the invasion of Poland.
World War II|Dunkirk evacuation begins|1940-05-26|Operation Dynamo began on 26 May 1940.
World War II|Battle of Britain|1940|The air campaign took place in 1940.
World War II|Germany invades Soviet Union|1941-06-22|Operation Barbarossa began in June 1941.
World War II|Attack on Pearl Harbor|1941-12-07|Japan attacked the US naval base in Hawaii.
World War II|D-Day Normandy landings|1944-06-06|Allied troops landed in Normandy.
World War II|Auschwitz liberated|1945-01-27|Soviet forces liberated Auschwitz.
World War II|VE Day|1945-05-08|Victory in Europe was marked on 8 May 1945.
World War II|Atomic bomb dropped on Hiroshima|1945-08-06|The United States dropped an atomic bomb on Hiroshima.
World War II|Atomic bomb dropped on Nagasaki|1945-08-09|The United States dropped a second atomic bomb.
World War II|Japan formally surrenders|1945-09-02|Japan signed the surrender instrument.
Modern Ireland & World|United Nations founded|1945-10-24|The UN Charter entered into force.
Modern Ireland & World|Republic of Ireland Act takes effect|1949-04-18|The state was formally described as a republic.
Modern Ireland & World|NATO established|1949-04-04|The North Atlantic Treaty was signed.
Modern Ireland & World|Treaty of Rome signed|1957-03-25|The treaty established the EEC.
Modern Ireland & World|Berlin Wall construction begins|1961-08-13|East German authorities began sealing the border.
Modern Ireland & World|Civil Rights march in Derry attacked|1968-10-05|A civil rights march was attacked by police in Derry.
Modern Ireland & World|Apollo 11 Moon landing|1969-07-20|Neil Armstrong and Buzz Aldrin landed on the Moon.
Modern Ireland & World|Bloody Sunday in Derry|1972-01-30|British soldiers shot civil rights marchers in Derry.
Modern Ireland & World|Ireland joins the EEC|1973-01-01|Ireland became a member of the European Economic Community.
Modern Ireland & World|Berlin Wall opens|1989-11-09|East German border crossings opened in November 1989.
Modern Ireland & World|Soviet Union dissolves|1991-12-26|The Soviet Union formally ceased to exist.
Modern Ireland & World|Good Friday Agreement signed|1998-04-10|The agreement was reached on Good Friday.
Modern Ireland & World|Euro notes and coins introduced in Ireland|2002-01-01|Euro cash entered circulation in 2002.'''
questions=[]
for idx,line in enumerate(raw.splitlines(),1):
 cat,title,date,exp=line.split('|')
 bce=' BCE' in date
 d=date.replace(' BCE','')
 parts=d.split('-')
 if bce: year=-int(parts[0]);month=None;day=None
 else: year=int(parts[0]);month=int(parts[1]) if len(parts)>1 else None;day=int(parts[2]) if len(parts)>2 else None
 questions.append(dict(id=f'hist-{idx:03}',subject='history',category=cat,question='When did '+title[0].lower()+title[1:]+'?',title=title,year=year,month=month,day=day,precision='day' if day else 'year',explanation=exp,tier='essential' if idx%3 else 'extended',source='Curated historical reference; verify against class notes'))
open('/mnt/data/history-quest/questions.js','w').write('window.BUILTIN_QUESTIONS='+json.dumps(questions,ensure_ascii=False,separators=(',',':'))+';\n')
print('Questions:',len(questions))
