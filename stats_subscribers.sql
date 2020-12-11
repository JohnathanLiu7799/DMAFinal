#Find Conversion Rate of Trial

SELECT COUNT(*) FROM subscribers
WHERE trial_completed = 1
AND current_sub_TF = 1;

#129354

SELECT COUNT(*) FROM subscribers
WHERE trial_completed = 1
AND current_sub_TF = 0;

#70882

#200236
#129354/200236 = ~64.6007 Conversion Rate

SELECT COUNT(*) FROM subscribers
WHERE male_TF = 1
AND male_TF != "";

#26457

SELECT COUNT(*) FROM subscribers
WHERE male_TF = 0
AND male_TF != "";

#201171

#11.62 % = Male
#88.25 % = Female

SELECT preferred_genre, COUNT(*) FROM subscribers
GROUP BY preferred_genre;

#None           36326       15.94%
#comedy         125129      54.92%
#drama          46872       20.57%
#international  6404        2.81%
#other          3907        1.71%
#regional       8990        3.94%

#Average age
SELECT AVG(age) FROM subscribers;

#46.12

SELECT country, COUNT(*) FROM subscribers
GROUP BY country;

#All UAE makes sense

SELECT attribution_technical, COUNT(*) FROM subscribers
GROUP BY attribution_technical
ORDER BY COUNT(*) DESC; 

/* 
facebook                 80251      35%
email                    25690
search                   25306
organic                  22013
brand sem intent google  18524
google_organic           10691
affiliate                9894
email_blast              7277
pinterest                6065
referral                 5170
facebook_organic         3272
discovery                2571
brand sem intent bing    2231
other                    1786
display                  1407
bing                     1146
internal                 1122
podcast                  985
youtube                  913
bing_organic             369
vod                      297
ott                      158
direct_mail              139
quora                    100
samsung                  86
criteo                   44
appstore                 44
pinterest_organic        30
influencer               21
playstore                12
twitter                  5
content_greatist         5
tv                       4 */

SELECT op_sys, COUNT(*) FROM subscribers
GROUP BY op_sys
ORDER BY COUNT(*) DESC;
/* 
iOS      143921     63.22%
Android  70332      30.89
         13375      NEED TO CLARIFY IF THIS = SMART TVs?
          */

SELECT strftime('%Y %m',account_creation_date) AS acc_date, COUNT(*) FROM subscribers
GROUP BY acc_date;
/* 
2019 06   2663
2019 07   25708
2019 08   25434
2019 09   20190
2019 10   22412
2019 11   26828
2019 12   25339
2020 01   24843
2020 02   28089
2020 03   26122
 */

 SELECT package_type, COUNT(*) FROM subscribers
 GROUP BY package_type;
/* 
                35574
base            111464      48.96
economy         17349
enhanced        63241 */

SELECT AVG(weekly_consumption_hour) FROM subscribers;

#23.33

SELECT plan_type, COUNT(*) FROM subscribers
GROUP BY plan_type;
/* 
base_eur_14_day_trial              18
base_uae_14_day_trial              227096
base_uae_no_trial_7_day_guarantee  1
high_aud_14_day_trial              2
high_jpy_14_day_trial              1
high_sar_14_day_trial              12
high_uae_14_day_trial              325
low_eur_no_trial                   1
low_gbp_14_day_trial               4
low_sar_no_trial                   1
low_uae_no_trial                   167 */

SELECT 

