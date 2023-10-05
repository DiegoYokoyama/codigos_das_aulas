create database healthcare character set utf8mb4 collate utf8mb4_unicode_ci;
use healthcare;

create table Countries(
country_name varchar(200) not null,
country_id int auto_increment primary key
);

create table Healthcare_Prices(
country_id int not null,
constraint foreign key (country_id) references Countries(country_id),
prices float not null
);

create table Global_Rank(
country_id int not null,
constraint foreign key (country_id) references Countries(country_id),
global_rank int not null primary key
);

create table Available_Date(
country_id int not null,
constraint foreign key (country_id) references Countries(country_id),
dates varchar(200) not null
);


Insert into Countries (country_name) values (	"	Switzerland	"),
	("	Bermuda	"),
	("	Iceland	"),
	("	Norway	"),
	("	Sweden	"),
	("	Israel	"),
	("	USA	"),
	("	Ireland	"),
	("	Bahamas	"),
	("	Luxembourg	"),
	("	Australia	"),
	("	Finland	"),
	("	Denmark	"),
	("	Barbados	"),
	("	Netherlands	"),
	("	Hong Kong	"),
	("	Austria	"),
	("	Singapore	"),
	("	UK	"),
	("	Italy	"),
	("	Costa Rica	"),
	("	Belgium	"),
	("	Canada	"),
	("	Uruguay	"),
	("	Japan	"),
	("	Spain	"),
	("	New Zealand	"),
	("	Germany	"),
	("	Cyprus	"),
	("	France	"),
	("	Brazil	"),
	("	Aruba	"),
	("	Montserrat	"),
	("	UA Emirates	"),
	("	Kuwait	"),
	("	Tr.&Tobago	"),
	("	Saint Lucia	"),
	("	Ant.& Barb.	"),
	("	Greece	"),
	("	Chile	"),
	("	Qatar	"),
	("	Malta	"),
	("	Slovenia	"),
	("	Portugal	"),
	("	Panama	"),
	("	Oman	"),
	("	Angola	"),
	("	Honduras	"),
	("	Djibouti	"),
	("	South Korea	"),
	("	Bahrain	"),
	("	Mexico	"),
	("	Belize	"),
	("	Dominica	"),
	("	Swaziland	"),
	("	St. Vincent & ...	"),
	("	Grenada	"),
	("	Estonia	"),
	("	South Africa	"),
	("	Namibia	"),
	("	Brunei	"),
	("	Mauritius	"),
	("	Ecuador	"),
	("	Argentina	"),
	("	Saudi Arabia	"),
	("	Seychelles	"),
	("	Gabon	"),
	("	Ivory Coast	"),
	("	China	"),
	("	Morocco	"),
	("	Iraq	"),
	("	El Salvador	"),
	("	Peru	"),
	("	Lesotho	"),
	("	Croatia	"),
	("	Eq. Guinea	"),
	("	Guyana	"),
	("	Slovakia	"),
	("	Cameroon	"),
	("	Domin. Rep.	"),
	("	Niger	"),
	("	Haiti	"),
	("	R. of Congo	"),
	("	Paraguay	"),
	("	Hungary	"),
	("	Malaysia	"),
	("	Chad	"),
	("	Latvia	"),
	("	Jordan	"),
	("	C.A. Republic	"),
	("	Maldives	"),
	("	Lithuania	"),
	("	Fiji	"),
	("	Mali	"),
	("	Poland	"),
	("	Togo	"),
	("	Bolivia	"),
	("	Botswana	"),
	("	Bosnia & Herz.	"),
	("	Zimbabwe	"),
	("	Guinea	"),
	("	Philippines	"),
	("	Cape Verde	"),
	("	Jamaica	"),
	("	Taiwan	"),
	("	Czechia	"),
	("	Colombia	"),
	("	Ghana	"),
	("	Rwanda	"),
	("	DR Congo	"),
	("	Comoros	"),
	("	Malawi	"),
	("	Thailand	"),
	("	Burundi	"),
	("	Mozambique	"),
	("	Mauritania	"),
	("	Benin	"),
	("	Tunisia	"),
	("	Senegal	"),
	("	Kenya	"),
	("	Liberia	"),
	("	G.-Bissau	"),
	("	S.T.&Principe	"),
	("	Burkina Faso	"),
	("	Suriname	"),
	("	Montenegro	"),
	("	Zambia	"),
	("	Madagascar	"),
	("	Nigeria	"),
	("	Iran	"),
	("	Gambia	"),
	("	Russia	"),
	("	Indonesia	"),
	("	Nicaragua	"),
	("	Armenia	"),
	("	Algeria	"),
	("	Bangladesh	"),
	("	Georgia	"),
	("	Serbia	"),
	("	Romania	"),
	("	Bulgaria	"),
	("	Pakistan	"),
	("	Vietnam	"),
	("	Sierra Leone	"),
	("	North Macedonia	"),
	("	Moldova	"),
	("	Tanzania	"),
	("	Cambodia	"),
	("	Kazakhstan	"),
	("	Ethiopia	"),
	("	Kyrgyzstan	"),
	("	Turkey	"),
	("	Tajikistan	"),
	("	Belarus	"),
	("	Uganda	"),
	("	Azerbaijan	"),
	("	Mongolia	"),
	("	India	"),
	("	Albania	"),
	("	Laos	"),
	("	Burma	"),
	("	Nepal	"),
	("	Sri Lanka	"),
	("	Bhutan	"),
	("	Egypt	"),
	("	Sudan	"),
	("	Ukraine	");
    

Insert into Healthcare_Prices values (	1	,	241.55	),
(	2	,	228.75	),
(	3	,	228.54	),
(	4	,	198.81	),
(	5	,	189.48	),
(	6	,	186.3	),
(	7	,	179.52	),
(	8	,	177.7	),
(	9	,	170.78	),
(	10	,	164.28	),
(	11	,	163.44	),
(	12	,	150.05	),
(	13	,	147.83	),
(	14	,	146.66	),
(	15	,	142.84	),
(	16	,	138.09	),
(	17	,	136.98	),
(	18	,	136.56	),
(	19	,	136.42	),
(	20	,	135.99	),
(	21	,	131.92	),
(	22	,	128.34	),
(	23	,	127.09	),
(	24	,	124.42	),
(	25	,	122.84	),
(	26	,	121.63	),
(	27	,	118.85	),
(	28	,	112.67	),
(	29	,	109.91	),
(	30	,	109.69	),
(	31	,	108.45	),
(	32	,	106.78	),
(	33	,	102.06	),
(	34	,	100.38	),
(	35	,	97.43	),
(	36	,	96.79	),
(	37	,	95.59	),
(	38	,	95.32	),
(	39	,	95.17	),
(	40	,	94.72	),
(	41	,	92.45	),
(	42	,	91.88	),
(	43	,	90	),
(	44	,	89.41	),
(	45	,	88.8	),
(	46	,	81.5	),
(	47	,	81.24	),
(	48	,	79.36	),
(	49	,	78.98	),
(	50	,	78.79	),
(	51	,	78.14	),
(	52	,	77.5	),
(	53	,	76.59	),
(	54	,	74.92	),
(	55	,	73.31	),
(	56	,	72.38	),
(	57	,	72.22	),
(	58	,	71.8	),
(	59	,	71.11	),
(	60	,	69.59	),
(	61	,	68.67	),
(	62	,	68.48	),
(	63	,	67.88	),
(	64	,	67.49	),
(	65	,	67.05	),
(	66	,	66.34	),
(	67	,	64.92	),
(	68	,	62.72	),
(	69	,	61.64	),
(	70	,	61.03	),
(	71	,	60.89	),
(	72	,	59.68	),
(	73	,	59.47	),
(	74	,	58.73	),
(	75	,	58.08	),
(	76	,	57.46	),
(	77	,	57.21	),
(	78	,	56.89	),
(	79	,	56.64	),
(	80	,	56.62	),
(	81	,	55.68	),
(	82	,	55.23	),
(	83	,	54.25	),
(	84	,	52.8	),
(	85	,	52.59	),
(	86	,	51.61	),
(	87	,	51.53	),
(	88	,	51.26	),
(	89	,	49.84	),
(	90	,	49.57	),
(	91	,	49.28	),
(	92	,	49.17	),
(	93	,	49.03	),
(	94	,	48.95	),
(	95	,	48.62	),
(	96	,	48.58	),
(	97	,	48.48	),
(	98	,	48.25	),
(	99	,	47.91	),
(	100	,	47.54	),
(	101	,	47.21	),
(	102	,	47.07	),
(	103	,	46.67	),
(	104	,	46.67	),
(	105	,	46.6	),
(	106	,	46.54	),
(	107	,	45.51	),
(	108	,	45.36	),
(	109	,	45.27	),
(	110	,	45.22	),
(	111	,	45.04	),
(	112	,	44.06	),
(	113	,	43.3	),
(	114	,	43.18	),
(	115	,	43.18	),
(	116	,	42.93	),
(	117	,	42.63	),
(	118	,	42.49	),
(	119	,	42.36	),
(	120	,	41.15	),
(	121	,	39.82	),
(	122	,	38.57	),
(	123	,	38.33	),
(	124	,	38.07	),
(	125	,	37.9	),
(	126	,	37.68	),
(	127	,	37.42	),
(	128	,	35.82	),
(	129	,	35.8	),
(	130	,	35.59	),
(	131	,	35.37	),
(	132	,	34.94	),
(	133	,	34.05	),
(	134	,	33.6	),
(	135	,	33.24	),
(	136	,	33.2	),
(	137	,	33.09	),
(	138	,	32.97	),
(	139	,	32.92	),
(	140	,	32.88	),
(	141	,	32.03	),
(	142	,	31.71	),
(	143	,	31.42	),
(	144	,	31.3	),
(	145	,	31.26	),
(	146	,	31.23	),
(	147	,	31.11	),
(	148	,	30.95	),
(	149	,	30.55	),
(	150	,	29.84	),
(	151	,	29.13	),
(	152	,	28.66	),
(	153	,	28.46	),
(	154	,	26.83	),
(	155	,	26.83	),
(	156	,	26.68	),
(	157	,	24.95	),
(	158	,	24.62	),
(	159	,	24.17	),
(	160	,	22.3	),
(	161	,	22.18	),
(	162	,	22.07	),
(	163	,	19.65	),
(	164	,	18.71	),
(	165	,	18.61	),
(	166	,	17.28	),
(	167	,	14.37);	


Insert into Global_Rank values (	1	,	1	),
(	2	,	2	),
(	3	,	3	),
(	4	,	4	),
(	5	,	5	),
(	6	,	6	),
(	7	,	7	),
(	8	,	8	),
(	9	,	9	),
(	10	,	10	),
(	11	,	11	),
(	12	,	12	),
(	13	,	13	),
(	14	,	14	),
(	15	,	15	),
(	16	,	16	),
(	17	,	17	),
(	18	,	18	),
(	19	,	19	),
(	20	,	20	),
(	21	,	21	),
(	22	,	22	),
(	23	,	23	),
(	24	,	24	),
(	25	,	25	),
(	26	,	26	),
(	27	,	27	),
(	28	,	28	),
(	29	,	29	),
(	30	,	30	),
(	31	,	31	),
(	32	,	32	),
(	33	,	33	),
(	34	,	34	),
(	35	,	35	),
(	36	,	36	),
(	37	,	37	),
(	38	,	38	),
(	39	,	39	),
(	40	,	40	),
(	41	,	41	),
(	42	,	42	),
(	43	,	43	),
(	44	,	44	),
(	45	,	45	),
(	46	,	46	),
(	47	,	47	),
(	48	,	48	),
(	49	,	49	),
(	50	,	50	),
(	51	,	51	),
(	52	,	52	),
(	53	,	53	),
(	54	,	54	),
(	55	,	55	),
(	56	,	56	),
(	57	,	57	),
(	58	,	58	),
(	59	,	59	),
(	60	,	60	),
(	61	,	61	),
(	62	,	62	),
(	63	,	63	),
(	64	,	64	),
(	65	,	65	),
(	66	,	66	),
(	67	,	67	),
(	68	,	68	),
(	69	,	69	),
(	70	,	70	),
(	71	,	71	),
(	72	,	72	),
(	73	,	73	),
(	74	,	74	),
(	75	,	75	),
(	76	,	76	),
(	77	,	77	),
(	78	,	78	),
(	79	,	79	),
(	80	,	80	),
(	81	,	81	),
(	82	,	82	),
(	83	,	83	),
(	84	,	84	),
(	85	,	85	),
(	86	,	86	),
(	87	,	87	),
(	88	,	88	),
(	89	,	89	),
(	90	,	90	),
(	91	,	91	),
(	92	,	92	),
(	93	,	93	),
(	94	,	94	),
(	95	,	95	),
(	96	,	96	),
(	97	,	97	),
(	98	,	98	),
(	99	,	99	),
(	100	,	100	),
(	101	,	101	),
(	102	,	102	),
(	103	,	103	),
(	104	,	104	),
(	105	,	105	),
(	106	,	106	),
(	107	,	107	),
(	108	,	108	),
(	109	,	109	),
(	110	,	110	),
(	111	,	111	),
(	112	,	112	),
(	113	,	113	),
(	114	,	114	),
(	115	,	115	),
(	116	,	116	),
(	117	,	117	),
(	118	,	118	),
(	119	,	119	),
(	120	,	120	),
(	121	,	121	),
(	122	,	122	),
(	123	,	123	),
(	124	,	124	),
(	125	,	125	),
(	126	,	126	),
(	127	,	127	),
(	128	,	128	),
(	129	,	129	),
(	130	,	130	),
(	131	,	131	),
(	132	,	132	),
(	133	,	133	),
(	134	,	134	),
(	135	,	135	),
(	136	,	136	),
(	137	,	137	),
(	138	,	138	),
(	139	,	139	),
(	140	,	140	),
(	141	,	141	),
(	142	,	142	),
(	143	,	143	),
(	144	,	144	),
(	145	,	145	),
(	146	,	146	),
(	147	,	147	),
(	148	,	148	),
(	149	,	149	),
(	150	,	150	),
(	151	,	151	),
(	152	,	152	),
(	153	,	153	),
(	154	,	154	),
(	155	,	155	),
(	156	,	156	),
(	157	,	157	),
(	158	,	158	),
(	159	,	159	),
(	160	,	160	),
(	161	,	161	),
(	162	,	162	),
(	163	,	163	),
(	164	,	164	),
(	165	,	165	),
(	166	,	166	),
(	167	,	167);	


Insert into Available_Date values (	1	,	"	2017 - 2017	"	),
(	2	,	"	2017 - 2017	"	),
(	3	,	"	2017 - 2017	"	),
(	4	,	"	2017 - 2017	"	),
(	5	,	"	2017 - 2017	"	),
(	6	,	"	2017 - 2017	"	),
(	7	,	"	2017 - 2017	"	),
(	8	,	"	2017 - 2017	"	),
(	9	,	"	2017 - 2017	"	),
(	10	,	"	2017 - 2017	"	),
(	11	,	"	2017 - 2017	"	),
(	12	,	"	2017 - 2017	"	),
(	13	,	"	2017 - 2017	"	),
(	14	,	"	2017 - 2017	"	),
(	15	,	"	2017 - 2017	"	),
(	16	,	"	2017 - 2017	"	),
(	17	,	"	2017 - 2017	"	),
(	18	,	"	2017 - 2017	"	),
(	19	,	"	2017 - 2017	"	),
(	20	,	"	2017 - 2017	"	),
(	21	,	"	2017 - 2017	"	),
(	22	,	"	2017 - 2017	"	),
(	23	,	"	2017 - 2017	"	),
(	24	,	"	2017 - 2017	"	),
(	25	,	"	2017 - 2017	"	),
(	26	,	"	2017 - 2017	"	),
(	27	,	"	2017 - 2017	"	),
(	28	,	"	2017 - 2017	"	),
(	29	,	"	2017 - 2017	"	),
(	30	,	"	2017 - 2017	"	),
(	31	,	"	2017 - 2017	"	),
(	32	,	"	2017 - 2017	"	),
(	33	,	"	2017 - 2017	"	),
(	34	,	"	2017 - 2017	"	),
(	35	,	"	2017 - 2017	"	),
(	36	,	"	2017 - 2017	"	),
(	37	,	"	2017 - 2017	"	),
(	38	,	"	2017 - 2017	"	),
(	39	,	"	2017 - 2017	"	),
(	40	,	"	2017 - 2017	"	),
(	41	,	"	2017 - 2017	"	),
(	42	,	"	2017 - 2017	"	),
(	43	,	"	2017 - 2017	"	),
(	44	,	"	2017 - 2017	"	),
(	45	,	"	2017 - 2017	"	),
(	46	,	"	2017 - 2017	"	),
(	47	,	"	2017 - 2017	"	),
(	48	,	"	2017 - 2017	"	),
(	49	,	"	2017 - 2017	"	),
(	50	,	"	2017 - 2017	"	),
(	51	,	"	2017 - 2017	"	),
(	52	,	"	2017 - 2017	"	),
(	53	,	"	2017 - 2017	"	),
(	54	,	"	2017 - 2017	"	),
(	55	,	"	2017 - 2017	"	),
(	56	,	"	2017 - 2017	"	),
(	57	,	"	2017 - 2017	"	),
(	58	,	"	2017 - 2017	"	),
(	59	,	"	2017 - 2017	"	),
(	60	,	"	2017 - 2017	"	),
(	61	,	"	2017 - 2017	"	),
(	62	,	"	2017 - 2017	"	),
(	63	,	"	2017 - 2017	"	),
(	64	,	"	2017 - 2017	"	),
(	65	,	"	2017 - 2017	"	),
(	66	,	"	2017 - 2017	"	),
(	67	,	"	2017 - 2017	"	),
(	68	,	"	2017 - 2017	"	),
(	69	,	"	2017 - 2017	"	),
(	70	,	"	2017 - 2017	"	),
(	71	,	"	2017 - 2017	"	),
(	72	,	"	2017 - 2017	"	),
(	73	,	"	2017 - 2017	"	),
(	74	,	"	2017 - 2017	"	),
(	75	,	"	2017 - 2017	"	),
(	76	,	"	2017 - 2017	"	),
(	77	,	"	2017 - 2017	"	),
(	78	,	"	2017 - 2017	"	),
(	79	,	"	2017 - 2017	"	),
(	80	,	"	2017 - 2017	"	),
(	81	,	"	2017 - 2017	"	),
(	82	,	"	2017 - 2017	"	),
(	83	,	"	2017 - 2017	"	),
(	84	,	"	2017 - 2017	"	),
(	85	,	"	2017 - 2017	"	),
(	86	,	"	2017 - 2017	"	),
(	87	,	"	2017 - 2017	"	),
(	88	,	"	2017 - 2017	"	),
(	89	,	"	2017 - 2017	"	),
(	90	,	"	2017 - 2017	"	),
(	91	,	"	2017 - 2017	"	),
(	92	,	"	2017 - 2017	"	),
(	93	,	"	2017 - 2017	"	),
(	94	,	"	2017 - 2017	"	),
(	95	,	"	2017 - 2017	"	),
(	96	,	"	2017 - 2017	"	),
(	97	,	"	2017 - 2017	"	),
(	98	,	"	2017 - 2017	"	),
(	99	,	"	2017 - 2017	"	),
(	100	,	"	2017 - 2017	"	),
(	101	,	"	2017 - 2017	"	),
(	102	,	"	2017 - 2017	"	),
(	103	,	"	2017 - 2017	"	),
(	104	,	"	2017 - 2017	"	),
(	105	,	"	2017 - 2017	"	),
(	106	,	"	2017 - 2017	"	),
(	107	,	"	2017 - 2017	"	),
(	108	,	"	2017 - 2017	"	),
(	109	,	"	2017 - 2017	"	),
(	110	,	"	2017 - 2017	"	),
(	111	,	"	2017 - 2017	"	),
(	112	,	"	2017 - 2017	"	),
(	113	,	"	2017 - 2017	"	),
(	114	,	"	2017 - 2017	"	),
(	115	,	"	2017 - 2017	"	),
(	116	,	"	2017 - 2017	"	),
(	117	,	"	2017 - 2017	"	),
(	118	,	"	2017 - 2017	"	),
(	119	,	"	2017 - 2017	"	),
(	120	,	"	2017 - 2017	"	),
(	121	,	"	2017 - 2017	"	),
(	122	,	"	2017 - 2017	"	),
(	123	,	"	2017 - 2017	"	),
(	124	,	"	2017 - 2017	"	),
(	125	,	"	2017 - 2017	"	),
(	126	,	"	2017 - 2017	"	),
(	127	,	"	2017 - 2017	"	),
(	128	,	"	2017 - 2017	"	),
(	129	,	"	2017 - 2017	"	),
(	130	,	"	2017 - 2017	"	),
(	131	,	"	2017 - 2017	"	),
(	132	,	"	2017 - 2017	"	),
(	133	,	"	2017 - 2017	"	),
(	134	,	"	2017 - 2017	"	),
(	135	,	"	2017 - 2017	"	),
(	136	,	"	2017 - 2017	"	),
(	137	,	"	2017 - 2017	"	),
(	138	,	"	2017 - 2017	"	),
(	139	,	"	2017 - 2017	"	),
(	140	,	"	2017 - 2017	"	),
(	141	,	"	2017 - 2017	"	),
(	142	,	"	2017 - 2017	"	),
(	143	,	"	2017 - 2017	"	),
(	144	,	"	2017 - 2017	"	),
(	145	,	"	2017 - 2017	"	),
(	146	,	"	2017 - 2017	"	),
(	147	,	"	2017 - 2017	"	),
(	148	,	"	2017 - 2017	"	),
(	149	,	"	2017 - 2017	"	),
(	150	,	"	2017 - 2017	"	),
(	151	,	"	2017 - 2017	"	),
(	152	,	"	2017 - 2017	"	),
(	153	,	"	2017 - 2017	"	),
(	154	,	"	2017 - 2017	"	),
(	155	,	"	2017 - 2017	"	),
(	156	,	"	2017 - 2017	"	),
(	157	,	"	2017 - 2017	"	),
(	158	,	"	2017 - 2017	"	),
(	159	,	"	2017 - 2017	"	),
(	160	,	"	2017 - 2017	"	),
(	161	,	"	2017 - 2017	"	),
(	162	,	"	2017 - 2017	"	),
(	163	,	"	2017 - 2017	"	),
(	164	,	"	2017 - 2017	"	),
(	165	,	"	2017 - 2017	"	),
(	166	,	"	2017 - 2017	"	),
(	167	,	"	2017 - 2017	");	
