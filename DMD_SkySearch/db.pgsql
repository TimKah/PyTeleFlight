--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: airlines; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE airlines (
    airlines_id integer NOT NULL,
    name text NOT NULL,
    telephone text NOT NULL,
    address text NOT NULL
);


ALTER TABLE airlines OWNER TO postgres;

--
-- Name: airlinesfeedback; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE airlinesfeedback (
    usersfeedback_id integer NOT NULL,
    text text NOT NULL,
    grade integer NOT NULL,
    user_id integer NOT NULL,
    airlines_id integer NOT NULL
);


ALTER TABLE airlinesfeedback OWNER TO postgres;

--
-- Name: airports; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE airports (
    airport_id integer NOT NULL,
    city_id integer NOT NULL,
    name character(50) NOT NULL
);


ALTER TABLE airports OWNER TO postgres;

--
-- Name: cities; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cities (
    city_id integer NOT NULL,
    name character(50) NOT NULL,
    country_id integer NOT NULL
);


ALTER TABLE cities OWNER TO postgres;

--
-- Name: citiesfeedback; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE citiesfeedback (
    usersfeedback_id integer NOT NULL,
    text text NOT NULL,
    grade integer NOT NULL,
    user_id integer NOT NULL,
    cities_id integer NOT NULL
);


ALTER TABLE citiesfeedback OWNER TO postgres;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE countries (
    country_id integer NOT NULL,
    name character(70) NOT NULL,
    geozone_id integer NOT NULL,
    capital integer
);


ALTER TABLE countries OWNER TO postgres;

--
-- Name: flights; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE flights (
    flight_id integer NOT NULL,
    duration integer NOT NULL,
    date_start date NOT NULL,
    date_end date NOT NULL,
    free_seats integer NOT NULL,
    airlines_id integer NOT NULL,
    city_from integer NOT NULL,
    city_to integer NOT NULL
);


ALTER TABLE flights OWNER TO postgres;

--
-- Name: geozone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE geozone (
    geozone_id integer NOT NULL,
    name character(50) NOT NULL
);


ALTER TABLE geozone OWNER TO postgres;

--
-- Name: notneedvisa; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE notneedvisa (
    visa_id integer NOT NULL,
    country_from integer NOT NULL,
    country_to integer NOT NULL,
    visa_condition boolean
);


ALTER TABLE notneedvisa OWNER TO postgres;

--
-- Name: recommendations; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE recommendations (
    recommendation_id integer NOT NULL,
    percantage integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE recommendations OWNER TO postgres;

--
-- Name: tickets; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tickets (
    ticket_number integer NOT NULL,
    user_id integer NOT NULL,
    flight_id integer NOT NULL
);


ALTER TABLE tickets OWNER TO postgres;

--
-- Name: timezone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE timezone (
    timezone_id integer NOT NULL,
    value integer NOT NULL,
    city_id integer NOT NULL
);


ALTER TABLE timezone OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    user_id integer NOT NULL,
    firstname character(30) NOT NULL,
    lastname character(50) NOT NULL,
    login character(50) NOT NULL,
    password character(50) NOT NULL,
    permanent_country character(70) NOT NULL,
    city integer,
    status character(30)
);


ALTER TABLE users OWNER TO postgres;

--
-- Data for Name: airlines; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY airlines (airlines_id, name, telephone, address) FROM stdin;
1	American Airlines Group1	(0113) 410 5670	611 Green Hill Street Nampa, ID 83651
2	Deutsche Lufthansa	(01668) 281678	66 Grandrose St.Honolulu, HI 96815
3	United Continental Holdings	(01565) 178168	9085 Bald Hill St. Jonesborough, TN 37659
4	Delta Air Lines	(01740) 743746	8857 Border Dr.Salt Lake City, UT 84119
5	Air France-KLM	(01372) 574212	113 Ring Rd, Leeds LS12 6AN
6	International Airlines Group2	(0118) 325 6065	Merrington Rd, Ferryhill DL17 8RW
7	Emirates	(01793) 633066	39 Byron St, Swindon SN1 3DQ
8	Southwest Airlines	(01438) 620554	4 Holyoake Ct, Bryan Rd, London SE16 5HJ
9	All Nippon Airways	(01688) 188473	227 Priory Rd, Eastbourne BN23 7TD
10	China Southern Airlines	(01206) 506852	5 Torloisk, Isle of Mull PA74 6NH
11	Aeroflot	(01880) 601137	23 Batavia Rd, Sunbury-on-Thames TW16 5LU
\.


--
-- Data for Name: airlinesfeedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY airlinesfeedback (usersfeedback_id, text, grade, user_id, airlines_id) FROM stdin;
\.


--
-- Data for Name: airports; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY airports (airport_id, city_id, name) FROM stdin;
1	1	DME                                               
2	1	VKO                                               
3	3	OVB                                               
4	8	KZN                                               
5	52	AER                                               
6	320	IAD                                               
7	321	JFK                                               
8	322	LAX                                               
9	323	BOS                                               
10	324	SFO                                               
11	325	DTW                                               
12	326	MDW                                               
13	327	LAS                                               
14	328	MIA                                               
15	329	STN                                               
16	330	EDI                                               
17	331	BRS                                               
18	332	BFS                                               
19	333	LPL                                               
20	334	CDG                                               
21	335	LIL                                               
22	336	MRS                                               
24	338	TXL                                               
25	339	HAM                                               
26	340	PEK                                               
27	341	HKG                                               
28	342	PVG                                               
29	343	HND                                               
30	344	OKA                                               
31	345	SKD                                               
32	346	TAS                                               
33	347	YOW                                               
34	348	YYZ                                               
35	349	YQB                                               
36	350	YUL                                               
37	351	SYD                                               
38	352	MEL                                               
39	353	PER                                               
\.


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cities (city_id, name, country_id) FROM stdin;
1	Moscow                                            	39
2	Saint Petersburg                                  	39
3	Novosibirsk                                       	39
4	Yekaterinburg                                     	39
5	Nizhny Novgorod                                   	39
6	Samara                                            	39
7	Omsk                                              	39
8	Kazan                                             	39
9	Chelyabinsk                                       	39
10	Rostov-on-Don                                     	39
11	Ufa                                               	39
12	Volgograd                                         	39
13	Perm                                              	39
14	Krasnoyarsk                                       	39
15	Voronezh                                          	39
16	Saratov                                           	39
17	Krasnodar                                         	39
18	Tolyatti                                          	39
19	Izhevsk                                           	39
20	Ulyanovsk                                         	39
21	Barnaul                                           	39
22	Vladivostok                                       	39
23	Yaroslavl                                         	39
24	Irkutsk                                           	39
25	Tyumen                                            	39
26	Khabarovsk                                        	39
27	Makhachkala                                       	39
28	Orenburg                                          	39
29	Novokuznetsk                                      	39
30	Kemerovo                                          	39
31	Ryazan                                            	39
32	Tomsk                                             	39
33	Astrakhan                                         	39
34	Penza                                             	39
35	Naberezhnye Chelny                                	39
36	Lipetsk                                           	39
37	Tula                                              	39
38	Kirov                                             	39
39	Cheboksary                                        	39
40	Kaliningrad                                       	39
41	Bryansk                                           	39
42	Kursk                                             	39
43	Ivanovo                                           	39
44	Magnitogorsk                                      	39
45	Ulan-Ude                                          	39
46	Tver                                              	39
47	Stavropol                                         	39
48	Nizhny Tagil                                      	39
49	Belgorod                                          	39
50	Arkhangelsk                                       	39
51	Vladimir                                          	39
52	Sochi                                             	39
53	Kurgan                                            	39
54	Smolensk                                          	39
55	Kaluga                                            	39
56	Chita                                             	39
57	Oryol                                             	39
58	Volzhsky                                          	39
59	Cherepovets                                       	39
60	Vladikavkaz                                       	39
61	Murmansk                                          	39
62	Surgut                                            	39
63	Vologda                                           	39
64	Saransk                                           	39
65	Tambov                                            	39
66	Sterlitamak                                       	39
67	Grozny                                            	39
68	Yakutsk                                           	39
69	Kostroma                                          	39
70	Komsomolsk-on-Amur                                	39
71	Petrozavodsk                                      	39
72	Taganrog                                          	39
73	Nizhnevartovsk                                    	39
74	Yoshkar-Ola                                       	39
75	Bratsk                                            	39
76	Novorossiysk                                      	39
77	Dzerzhinsk                                        	39
78	Nalchik                                           	39
79	Shakhty                                           	39
80	Orsk                                              	39
81	Syktyvkar                                         	39
82	Nizhnekamsk                                       	39
83	Angarsk                                           	39
84	Stary Oskol                                       	39
85	Veliky Novgorod                                   	39
86	Balashikha                                        	39
87	Blagoveshchensk                                   	39
88	Prokopyevsk                                       	39
89	Biysk                                             	39
90	Khimki                                            	39
91	Pskov                                             	39
92	Engels                                            	39
93	Rybinsk                                           	39
94	Balakovo                                          	39
95	Severodvinsk                                      	39
96	Armavir                                           	39
97	Podolsk                                           	39
98	Korolyov                                          	39
99	Yuzhno-Sakhalinsk                                 	39
100	Petropavlovsk-Kamchatsky                          	39
101	Syzran                                            	39
102	Norilsk                                           	39
103	Zlatoust                                          	39
104	Kamensk-Uralsky                                   	39
105	Mytishchi                                         	39
106	Lyubertsy                                         	39
107	Volgodonsk                                        	39
108	Novocherkassk                                     	39
109	Abakan                                            	39
110	Nakhodka                                          	39
111	Ussuriysk                                         	39
112	Berezniki                                         	39
113	Salavat                                           	39
114	Elektrostal                                       	39
115	Miass                                             	39
116	Rubtsovsk                                         	39
117	Almetyevsk                                        	39
118	Kovrov                                            	39
119	Kolomna                                           	39
120	Maykop                                            	39
121	Pyatigorsk                                        	39
122	Odintsovo                                         	39
123	Kopeysk                                           	39
124	Novomoskovsk                                      	39
125	Zheleznodorozhny                                  	39
126	Khasavyurt                                        	39
127	Cherkessk                                         	39
128	Kislovodsk                                        	39
129	Serpukhov                                         	39
130	Pervouralsk                                       	39
131	Novocheboksarsk                                   	39
132	Nefteyugansk                                      	39
133	Dimitrovgrad                                      	39
134	Neftekamsk                                        	39
135	Orekhovo-Zuyevo                                   	39
136	Kamyshin                                          	39
137	Derbent                                           	39
138	Nevinnomyssk                                      	39
139	Krasnogorsk                                       	39
140	Murom                                             	39
141	Bataysk                                           	39
142	Sergiyev Posad                                    	39
143	Novoshakhtinsk                                    	39
144	Noyabrsk                                          	39
145	Shchyolkovo                                       	39
146	Kyzyl                                             	39
147	Oktyabrsky                                        	39
148	Achinsk                                           	39
149	Seversk                                           	39
150	Novokuybyshevsk                                   	39
151	Yelets                                            	39
152	Arzamas                                           	39
153	Obninsk                                           	39
154	Zhukovsky                                         	39
155	Novy Urengoy                                      	39
156	Elista                                            	39
157	Pushkino                                          	39
158	Artyom                                            	39
159	Mezhdurechensk                                    	39
160	Leninsk-Kuznetsky                                 	39
161	Sarapul                                           	39
162	Yessentuki                                        	39
163	Kaspiysk                                          	39
164	Noginsk                                           	39
165	Tobolsk                                           	39
166	Ukhta                                             	39
167	Serov                                             	39
168	Votkinsk                                          	39
169	Velikiye Luki                                     	39
170	Michurinsk                                        	39
171	Kiselyovsk                                        	39
172	Novotroitsk                                       	39
173	Zelenodolsk                                       	39
174	Solikamsk                                         	39
175	Berdsk                                            	39
176	Ramenskoye                                        	39
177	Domodedovo                                        	39
178	Magadan                                           	39
179	Glazov                                            	39
180	Kamensk-Shakhtinsky                               	39
181	Zheleznogorsk                                     	39
182	Kansk                                             	39
183	Nazran                                            	39
184	Gatchina                                          	39
185	Sarov                                             	39
186	Voskresensk                                       	39
187	Dolgoprudny                                       	39
188	Bugulma                                           	39
189	Kuznetsk                                          	39
190	Gubkin                                            	39
191	Kineshma                                          	39
192	Yeysk                                             	39
193	Reutov                                            	39
194	Ust-Ilimsk                                        	39
195	Novouralsk                                        	39
196	Zheleznogorsk                                     	39
197	Usolye-Sibirskoye                                 	39
198	Azov                                              	39
199	Buzuluk                                           	39
200	Chaykovsky                                        	39
201	Balashov                                          	39
202	Ozyorsk                                           	39
203	Yurga                                             	39
204	Kirovo-Chepetsk                                   	39
205	Kropotkin                                         	39
206	Klin                                              	39
207	Khanty-Mansiysk                                   	39
208	Vyborg                                            	39
209	Troitsk                                           	39
210	Bor                                               	39
211	Shadrinsk                                         	39
212	Belovo                                            	39
213	Mineralnye Vody                                   	39
214	Anzhero-Sudzhensk                                 	39
215	Birobidzhan                                       	39
216	Lobnya                                            	39
217	Chapayevsk                                        	39
218	Georgiyevsk                                       	39
219	Chernogorsk                                       	39
220	Minusinsk                                         	39
221	Mikhaylovsk                                       	39
222	Yelabuga                                          	39
223	Dubna                                             	39
224	Vorkuta                                           	39
225	Novoaltaysk                                       	39
226	Yegoryevsk                                        	39
227	Asbest                                            	39
228	Beloretsk                                         	39
229	Belogorsk                                         	39
230	Gukovo                                            	39
231	Tuymazy                                           	39
232	Stupino                                           	39
233	Kstovo                                            	39
234	Volsk                                             	39
235	Ishimbay                                          	39
236	Kungur                                            	39
237	Zelenogorsk                                       	39
238	Lysva                                             	39
239	Sosnovy Bor                                       	39
240	Borisoglebsk                                      	39
241	Ishim                                             	39
242	Naro-Fominsk                                      	39
243	Budyonnovsk                                       	39
244	Donskoy                                           	39
245	Polevskoy                                         	39
246	Leninogorsk                                       	39
247	Slavyansk-na-Kubani                               	39
248	Pavlovsky Posad                                   	39
249	Zarechny                                          	39
250	Tuapse                                            	39
251	Rossosh                                           	39
252	Labinsk                                           	39
253	Kumertau                                          	39
254	Sibay                                             	39
255	Buynaksk                                          	39
256	Klintsy                                           	39
257	Rzhev                                             	39
258	Revda                                             	39
259	Tikhoretsk                                        	39
260	Neryungri                                         	39
261	Aleksin                                           	39
262	Alexandrov                                        	39
263	Meleuz                                            	39
264	Salsk                                             	39
265	Dmitrov                                           	39
266	Lesosibirsk                                       	39
267	Gus-Khrustalny                                    	39
268	Chistopol                                         	39
269	Chekhov                                           	39
270	Pavlovo                                           	39
271	Kotlas                                            	39
272	Belebey                                           	39
273	Iskitim                                           	39
274	Verkhnyaya Pyshma                                 	39
275	Vsevolozhsk                                       	39
276	Apatity                                           	39
277	Krasnoturyinsk                                    	39
278	Prokhladny                                        	39
279	Mikhaylovka                                       	39
280	Anapa                                             	39
281	Svobodny                                          	39
282	Ivanteyevka                                       	39
283	Shuya                                             	39
284	Tikhvin                                           	39
285	Kogalym                                           	39
286	Shchyokino                                        	39
287	Krymsk                                            	39
288	Vyazma                                            	39
289	Gorno-Altaysk                                     	39
290	Vidnoye                                           	39
291	Arsenyev                                          	39
292	Vyksa                                             	39
293	Klimovsk                                          	39
294	Liski                                             	39
295	Krasnokamensk                                     	39
296	Volzhsk                                           	39
297	Izberbash                                         	39
298	Zhigulyovsk                                       	39
299	Fryazino                                          	39
300	Uzlovaya                                          	39
301	Lytkarino                                         	39
302	Gelendzhik                                        	39
303	Roslavl                                           	39
304	Nyagan                                            	39
305	Timashyovsk                                       	39
306	Belorechensk                                      	39
307	Borovichi                                         	39
308	Solnechnogorsk                                    	39
309	Nazarovo                                          	39
310	Cheremkhovo                                       	39
311	Vyshny Volochyok                                  	39
312	Kirishi                                           	39
313	Krasnokamsk                                       	39
314	Beryozovsky                                       	39
315	Balakhna                                          	39
316	Lesnoy                                            	39
317	Livny                                             	39
318	Donetsk                                           	39
319	Severomorsk                                       	39
320	Washington                                        	85
321	New-York                                          	85
322	Los Angeles                                       	85
323	Boston                                            	85
324	San Francisco                                     	85
325	Detroyt                                           	85
326	Chicago                                           	85
327	Las Vegas                                         	85
328	Miami                                             	85
329	London                                            	85
330	Edinburgh                                         	85
331	Bristol                                           	85
332	Belfast                                           	85
333	Liverpool                                         	85
334	Paris                                             	85
335	Lille                                             	85
336	Marsel                                            	85
338	Berlin                                            	85
339	Hamburg                                           	85
340	Beijing                                           	85
341	Hong kong                                         	85
342	Shanhai                                           	85
343	Tokio                                             	85
344	Okinawa                                           	85
345	Samarkand                                         	85
346	Tashkent                                          	85
347	Ottawa                                            	85
348	Toronto                                           	85
349	Quebek                                            	85
350	Montreal                                          	85
351	Sydney                                            	85
352	Melbourne                                         	85
353	Perth                                             	85
0	Innopolis                                         	39
\.


--
-- Data for Name: citiesfeedback; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY citiesfeedback (usersfeedback_id, text, grade, user_id, cities_id) FROM stdin;
\.


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY countries (country_id, name, geozone_id, capital) FROM stdin;
39	Russia                                                                	7	1
1	Albania                                                               	2	\N
2	Bosnia and Herzegovina                                                	2	\N
3	Bulgaria                                                              	2	\N
4	Croatia                                                               	2	\N
5	Greece                                                                	2	\N
6	Republic of Macedonia                                                 	2	\N
7	Montenegro                                                            	2	\N
8	Romania                                                               	2	\N
9	Serbia                                                                	2	\N
10	Slovenia                                                              	2	\N
11	Turkey                                                                	2	\N
12	Estonia                                                               	3	\N
13	Latvia                                                                	3	\N
14	Lithuania?                                                            	3	\N
15	Denmark                                                               	4	\N
16	Finland                                                               	4	\N
17	Iceland                                                               	4	\N
18	Norway                                                                	4	\N
19	Sweden                                                                	4	\N
20	Armenia                                                               	6	\N
21	Azerbaijan                                                            	6	\N
22	Georgia                                                               	6	\N
23	Austria                                                               	5	\N
24	Czech Republic                                                        	5	\N
25	Germany                                                               	5	\N
26	Hungary                                                               	5	\N
27	Liechtenstein                                                         	5	\N
28	Poland                                                                	5	\N
29	Slovakia                                                              	5	\N
30	Slovenia                                                              	5	\N
31	Switzerland                                                           	5	\N
32	Denmark                                                               	7	\N
33	Estonia                                                               	7	\N
34	Finland                                                               	7	\N
35	Iceland                                                               	7	\N
36	Latvia                                                                	7	\N
37	Lithuania                                                             	7	\N
38	Norway                                                                	7	\N
40	Sweden                                                                	7	\N
41	Albania                                                               	9	\N
42	Bosnia and Herzegovina                                                	9	\N
43	Bulgaria                                                              	9	\N
44	Croatia                                                               	9	\N
45	Cyprus                                                                	9	\N
46	Greece                                                                	9	\N
47	Kosovo                                                                	9	\N
48	Republic of Macedonia                                                 	9	\N
49	Moldova                                                               	9	\N
50	Montenegro                                                            	9	\N
51	Romania                                                               	9	\N
52	Serbia                                                                	9	\N
53	Slovenia                                                              	9	\N
54	Turkey                                                                	9	\N
55	Bosnia and Herzegovina                                                	8	\N
56	Bulgaria                                                              	8	\N
57	Croatia                                                               	8	\N
58	Greece                                                                	8	\N
59	Kosovo                                                                	8	\N
60	Republic of Macedonia                                                 	8	\N
61	Montenegro                                                            	8	\N
62	Romania                                                               	8	\N
63	Serbia                                                                	8	\N
64	Slovenia                                                              	8	\N
65	Belgium                                                               	10	\N
66	France                                                                	10	\N
67	Luxembourg                                                            	10	\N
68	Netherlands                                                           	10	\N
69	United Kingdom                                                        	10	\N
70	Angola                                                                	13	\N
71	Namibia                                                               	13	\N
72	Mozambique                                                            	13	\N
73	Tanzania                                                              	13	\N
74	Swaziland                                                             	13	\N
75	Seychelles                                                            	13	\N
76	Mauritius                                                             	13	\N
77	Zambia                                                                	13	\N
78	Zimbabwe                                                              	13	\N
79	Botswana                                                              	13	\N
80	Democratic                                                            	13	\N
81	Republic of the Congo                                                 	13	\N
82	Lesotho                                                               	13	\N
83	Madagascar                                                            	13	\N
84	Malawi                                                                	13	\N
86	Mexico                                                                	12	\N
87	Canada                                                                	12	\N
88	Cuba                                                                  	12	\N
89	Dominican Republic                                                    	12	\N
90	Guatemala                                                             	12	\N
91	Panama                                                                	12	\N
92	Costa Rica                                                            	12	\N
93	El Salvador                                                           	12	\N
94	Trinidad and Tobago                                                   	12	\N
95	Honduras                                                              	12	\N
96	Nicaragua Nicaragua                                                   	12	\N
97	Jamaica Jamaica                                                       	12	\N
98	Haiti                                                                 	12	\N
99	The Bahamas                                                           	12	\N
100	Barbados                                                              	12	\N
101	Belize                                                                	12	\N
102	Antigua and Barbuda                                                   	12	\N
85	United States of America                                              	12	320
103	Saint Lucia                                                           	12	\N
104	Grenada                                                               	12	\N
105	Saint Kitts and Nevis                                                 	12	\N
106	Saint Vincent and the Grenadines                                      	12	\N
107	Dominica                                                              	12	\N
108	Australia                                                             	14	\N
109	Fiji                                                                  	14	\N
110	Kiribati                                                              	14	\N
111	Marshall Islands                                                      	14	\N
112	Micronesia                                                            	14	\N
113	Nauru                                                                 	14	\N
114	New Zealand                                                           	14	\N
115	Palau                                                                 	14	\N
116	Papua New Guinea                                                      	14	\N
117	Samoa                                                                 	14	\N
118	Solomon Islands                                                       	14	\N
119	Tonga                                                                 	14	\N
120	Tuvalu                                                                	14	\N
121	Vanuatu                                                               	14	\N
122	Argentina                                                             	11	\N
123	Bolivia                                                               	11	\N
124	Brazil                                                                	11	\N
125	Chile                                                                 	11	\N
126	Colombia                                                              	11	\N
127	Ecuador                                                               	11	\N
128	French Guiana                                                         	11	\N
129	Guyana                                                                	11	\N
130	Paraguay                                                              	11	\N
131	Peru                                                                  	11	\N
132	Suriname                                                              	11	\N
133	Uruguay                                                               	11	\N
134	Venezuela                                                             	11	\N
135	China                                                                 	2	\N
136	Japan                                                                 	2	\N
137	Laos                                                                  	2	\N
138	Pakistan                                                              	2	\N
139	Taiwan                                                                	2	\N
140	Korea                                                                 	2	\N
141	Thailand                                                              	2	\N
142	Uzbekistan                                                            	2	\N
143	Syria                                                                 	2	\N
\.


--
-- Data for Name: flights; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY flights (flight_id, duration, date_start, date_end, free_seats, airlines_id, city_from, city_to) FROM stdin;
1	10	2016-01-08	2016-01-08	19	2	72	54
2	6	2016-12-15	2016-12-15	57	3	256	34
3	10	2016-09-23	2016-09-23	51	7	244	203
4	9	2016-05-17	2016-05-17	7	7	176	308
5	9	2016-03-04	2016-03-04	49	3	263	194
6	7	2016-05-12	2016-05-13	15	6	310	186
7	7	2016-01-01	2016-01-01	29	4	55	248
8	10	2016-03-15	2016-03-15	22	10	257	78
9	3	2016-11-14	2016-11-14	42	8	66	151
10	10	2016-10-09	2016-10-09	3	9	121	28
11	9	2016-08-11	2016-08-11	63	6	75	284
12	2	2016-03-04	2016-03-04	55	5	224	270
13	10	2016-01-03	2016-01-04	35	2	226	63
14	4	2016-10-17	2016-10-17	18	1	334	149
15	5	2016-03-15	2016-03-15	34	10	65	137
16	8	2016-04-12	2016-04-12	49	9	268	194
17	3	2016-05-12	2016-05-12	51	3	142	343
18	8	2016-01-08	2016-01-08	32	7	131	296
19	6	2016-07-14	2016-07-14	16	10	35	315
20	10	2016-01-08	2016-01-08	19	2	72	54
21	6	2016-12-15	2016-12-15	57	3	72	34
22	10	2016-09-23	2016-09-23	51	7	72	203
23	9	2016-05-17	2016-05-17	7	7	176	308
24	9	2016-03-04	2016-03-04	49	3	176	194
25	7	2016-05-12	2016-05-13	15	6	55	186
26	7	2016-01-01	2016-01-01	29	4	55	248
27	10	2016-03-15	2016-03-15	22	10	55	78
28	3	2016-11-14	2016-11-14	42	8	66	151
29	10	2016-10-09	2016-10-09	3	9	66	28
30	9	2016-08-11	2016-08-11	63	6	75	284
31	2	2016-03-04	2016-03-04	55	5	75	270
\.


--
-- Data for Name: geozone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY geozone (geozone_id, name) FROM stdin;
1	Asia                                              
2	Balkan countries                                  
3	Baltic states                                     
4	Scandinavian countries                            
5	Central European countries                        
6	Eastern European countries                        
7	Northern European countries                       
8	Southeastern European countries                   
9	Southern European countries                       
10	Western European countries                        
11	South America                                     
12	North America                                     
13	Africa                                            
14	Australia and Oceania                             
897	ololo                                             
\.


--
-- Data for Name: notneedvisa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY notneedvisa (visa_id, country_from, country_to, visa_condition) FROM stdin;
1	39	16	t
2	39	17	t
3	39	18	t
4	39	19	t
5	39	20	f
6	39	23	t
7	39	24	t
8	39	25	t
9	39	26	t
10	39	27	t
11	39	28	t
12	39	29	t
13	39	30	t
14	39	83	t
15	39	89	f
16	39	90	f
17	39	91	f
18	39	122	f
19	39	123	t
20	39	124	f
21	39	107	f
22	39	108	t
23	39	87	t
24	39	85	t
25	25	66	f
26	26	66	f
27	27	66	f
28	54	66	t
\.


--
-- Data for Name: recommendations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY recommendations (recommendation_id, percantage, user_id) FROM stdin;
\.


--
-- Data for Name: tickets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tickets (ticket_number, user_id, flight_id) FROM stdin;
1	1	8
2	5	12
3	1	12
4	7	2
5	6	12
6	1	2
7	2	8
8	6	2
9	4	15
10	2	17
11	2	13
12	2	3
13	1	17
14	1	8
15	7	17
16	5	12
17	2	15
18	2	18
19	1	11
20	6	15
21	7	5
22	3	9
23	7	2
24	5	1
25	7	6
26	4	5
27	1	14
28	2	12
29	1	19
30	4	1
31	5	18
32	4	14
33	5	7
34	4	8
35	5	6
36	5	11
37	5	19
38	2	1
39	7	16
40	2	19
41	2	3
42	7	11
43	1	15
44	7	19
45	1	5
46	3	9
47	5	3
48	5	11
49	1	17
50	3	3
51	3	7
52	2	3
53	5	4
54	5	15
55	7	3
56	3	18
57	4	9
58	4	16
59	7	3
\.


--
-- Data for Name: timezone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY timezone (timezone_id, value, city_id) FROM stdin;
1	3	1
2	7	3
3	3	8
4	3	52
5	-5	320
6	-5	321
7	-8	322
8	-5	323
9	-8	324
10	-5	325
11	-6	326
12	-8	327
13	-5	328
14	1	329
15	0	330
16	0	331
17	0	332
18	0	333
19	1	334
20	2	335
21	2	336
22	1	339
23	1	340
24	8	341
25	8	342
26	8	343
27	9	344
28	9	345
29	5	346
30	5	347
31	-5	348
32	-5	349
33	-5	350
34	-5	351
35	10	352
36	11	353
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users (user_id, firstname, lastname, login, password, permanent_country, city, status) FROM stdin;
2	Elaine                        	kirill                                            	Pused1971                                         	kah9aeY7th                                        	Canada                                                                	\N	\N
3	James                         	kirill                                            	Dient1990                                         	wiaNuh7iax                                        	Russia                                                                	\N	\N
4	Nellie                        	kirill                                            	Safelip1974                                       	looD9cah5oP                                       	Russia                                                                	\N	\N
5	Shawn                         	kirill                                            	Loohn1967                                         	iQu9Dein                                          	Russia                                                                	\N	\N
6	Ramon                         	kirill                                            	Grine1976                                         	Eih4aivoc2i                                       	United Kingdom                                                        	\N	\N
1	Gordon                        	kir                                               	Denter52                                          	do8Eizeifa                                        	United States                                                         	1	\N
7	admin                         	kirill                                            	admin                                             	admin                                             	Russia                                                                	\N	\N
130396179	Dilyara                       	Akhsanova                                         	None                                              	None                                              	None                                                                  	72	escape                        
\.


--
-- Name: airlines_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY airlines
    ADD CONSTRAINT airlines_pk PRIMARY KEY (airlines_id);


--
-- Name: airlinesfeedback_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY airlinesfeedback
    ADD CONSTRAINT airlinesfeedback_pk PRIMARY KEY (usersfeedback_id);


--
-- Name: airports_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY airports
    ADD CONSTRAINT airports_pk PRIMARY KEY (airport_id);


--
-- Name: cities_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cities
    ADD CONSTRAINT cities_pk PRIMARY KEY (city_id);


--
-- Name: citiesfeedback_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY citiesfeedback
    ADD CONSTRAINT citiesfeedback_pk PRIMARY KEY (usersfeedback_id);


--
-- Name: countries_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY countries
    ADD CONSTRAINT countries_pk PRIMARY KEY (country_id);


--
-- Name: flights_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY flights
    ADD CONSTRAINT flights_pk PRIMARY KEY (flight_id);


--
-- Name: geozone_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY geozone
    ADD CONSTRAINT geozone_pk PRIMARY KEY (geozone_id);


--
-- Name: notneedvisa_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY notneedvisa
    ADD CONSTRAINT notneedvisa_pk PRIMARY KEY (visa_id);


--
-- Name: recommendations_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY recommendations
    ADD CONSTRAINT recommendations_pk PRIMARY KEY (recommendation_id);


--
-- Name: tickets_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tickets
    ADD CONSTRAINT tickets_pk PRIMARY KEY (ticket_number);


--
-- Name: timezone_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY timezone
    ADD CONSTRAINT timezone_pk PRIMARY KEY (timezone_id);


--
-- Name: users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pk PRIMARY KEY (user_id);


--
-- Name: airlinesfeedback_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY airlinesfeedback
    ADD CONSTRAINT airlinesfeedback_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: airlinesfeedback_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY airlinesfeedback
    ADD CONSTRAINT airlinesfeedback_fk1 FOREIGN KEY (airlines_id) REFERENCES airlines(airlines_id);


--
-- Name: airports_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY airports
    ADD CONSTRAINT airports_fk0 FOREIGN KEY (city_id) REFERENCES cities(city_id);


--
-- Name: cities_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cities
    ADD CONSTRAINT cities_fk0 FOREIGN KEY (country_id) REFERENCES countries(country_id);


--
-- Name: citiesfeedback_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY citiesfeedback
    ADD CONSTRAINT citiesfeedback_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: citiesfeedback_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY citiesfeedback
    ADD CONSTRAINT citiesfeedback_fk1 FOREIGN KEY (cities_id) REFERENCES cities(city_id);


--
-- Name: countries_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY countries
    ADD CONSTRAINT countries_fk0 FOREIGN KEY (geozone_id) REFERENCES geozone(geozone_id);


--
-- Name: countries_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY countries
    ADD CONSTRAINT countries_fk1 FOREIGN KEY (capital) REFERENCES cities(city_id);


--
-- Name: flights_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY flights
    ADD CONSTRAINT flights_fk0 FOREIGN KEY (airlines_id) REFERENCES airlines(airlines_id);


--
-- Name: flights_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY flights
    ADD CONSTRAINT flights_fk1 FOREIGN KEY (city_from) REFERENCES cities(city_id);


--
-- Name: flights_fk2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY flights
    ADD CONSTRAINT flights_fk2 FOREIGN KEY (city_to) REFERENCES cities(city_id);


--
-- Name: notneedvisa_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY notneedvisa
    ADD CONSTRAINT notneedvisa_fk0 FOREIGN KEY (country_from) REFERENCES countries(country_id);


--
-- Name: notneedvisa_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY notneedvisa
    ADD CONSTRAINT notneedvisa_fk1 FOREIGN KEY (country_to) REFERENCES countries(country_id);


--
-- Name: recommendations_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY recommendations
    ADD CONSTRAINT recommendations_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: tickets_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tickets
    ADD CONSTRAINT tickets_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: tickets_fk1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tickets
    ADD CONSTRAINT tickets_fk1 FOREIGN KEY (flight_id) REFERENCES flights(flight_id);


--
-- Name: timezone_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY timezone
    ADD CONSTRAINT timezone_fk0 FOREIGN KEY (city_id) REFERENCES cities(city_id);


--
-- Name: users_city_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_city_fkey FOREIGN KEY (city) REFERENCES cities(city_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: users.city; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL(city) ON TABLE users FROM PUBLIC;
REVOKE ALL(city) ON TABLE users FROM postgres;
GRANT REFERENCES(city) ON TABLE users TO PUBLIC;


--
-- PostgreSQL database dump complete
--

