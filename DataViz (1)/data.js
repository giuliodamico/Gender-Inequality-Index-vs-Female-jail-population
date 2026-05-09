// Embedded dataset — Gender Gap Index + female prison data (EU 2014–2023)
// Compiled from final_prison_data.csv

const REGIONS = {
  Northern: ['Finland','Sweden','Ireland','Denmark','Lithuania','Estonia'],
  Southern: ['Slovenia','Spain','Portugal','Croatia','Italy','Greece','Malta','Cyprus'],
  Western:  ['Germany','France','Belgium','Netherlands','Austria','Luxembourg'],
  Eastern:  ['Latvia','Bulgaria','Poland','Romania','Slovakia','Czechia','Hungary']
};

const REGION_COLORS = {
  Northern: '#003399',
  Southern: '#E74C3C',
  Western:  '#27AE60',
  Eastern:  '#8E44AD'
};

const COUNTRY_REGION = {};
Object.entries(REGIONS).forEach(([r, list]) => list.forEach(c => COUNTRY_REGION[c] = r));

// Country avg GGI 2014–2023 (computed)
const COUNTRY_AVG_GGI = {
  Finland:0.843, Sweden:0.819, Ireland:0.797, Denmark:0.775, Lithuania:0.759, Estonia:0.740,
  Slovenia:0.767, Spain:0.764, Portugal:0.745, Croatia:0.717, Italy:0.710, Greece:0.690, Malta:0.687, Cyprus:0.686,
  Germany:0.786, France:0.772, Belgium:0.763, Netherlands:0.752, Austria:0.738, Luxembourg:0.728,
  Latvia:0.771, Bulgaria:0.737, Poland:0.722, Romania:0.703, Slovakia:0.699, Czechia:0.694, Hungary:0.679
};

const EU_AVG = 0.742;
const YEARS = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023];

// GGI per country per year (from the CSV — Gender_index column)
const GGI = {
  Austria:     [0.7266,0.733,0.716,0.709,0.718,0.731,0.744,0.777,0.781,0.740],
  Belgium:     [0.7809,0.753,0.745,0.739,0.738,0.7445,0.751,0.789,0.793,0.796],
  Bulgaria:    [0.7444,0.722,0.726,0.756,0.756,0.7415,0.727,0.746,0.740,0.715],
  Croatia:     [0.7075,0.708,0.700,0.711,0.712,0.716,0.720,0.733,0.733,0.730],
  Cyprus:      [0.6741,0.671,0.684,0.684,0.684,0.688,0.692,0.707,0.696,0.678],
  Czechia:     [0.6737,0.687,0.690,0.688,0.693,0.6995,0.706,0.711,0.710,0.685],
  Denmark:     [0.8025,0.767,0.754,0.776,0.778,0.780,0.782,0.768,0.764,0.780],
  Estonia:     [0.7017,0.749,0.747,0.731,0.734,0.7425,0.751,0.733,0.733,0.782],
  Finland:     [0.8453,0.850,0.845,0.823,0.821,0.8265,0.832,0.861,0.860,0.863],
  France:      [0.7588,0.761,0.755,0.778,0.779,0.780,0.781,0.784,0.791,0.756],
  Germany:     [0.778,0.779,0.766,0.778,0.776,0.7815,0.787,0.796,0.801,0.815],
  Greece:      [0.6784,0.685,0.680,0.692,0.696,0.6985,0.701,0.689,0.689,0.693],
  Hungary:     [0.6759,0.672,0.669,0.670,0.674,0.6755,0.677,0.688,0.699,0.689],
  Ireland:     [0.785,0.807,0.797,0.794,0.796,0.797,0.798,0.800,0.804,0.795],
  Italy:       [0.6973,0.726,0.719,0.692,0.706,0.7065,0.707,0.721,0.720,0.705],
  Latvia:      [0.7691,0.752,0.775,0.756,0.758,0.7715,0.785,0.778,0.771,0.794],
  Lithuania:   [0.7208,0.740,0.744,0.742,0.749,0.747,0.745,0.804,0.799,0.800],
  Luxembourg:  [0.7333,0.738,0.734,0.707,0.712,0.7185,0.725,0.726,0.736,0.747],
  Malta:       [0.6707,0.668,0.664,0.682,0.686,0.6895,0.693,0.703,0.703,0.713],
  Netherlands: [0.773,0.776,0.756,0.737,0.747,0.7245,0.702,0.762,0.767,0.777],
  Poland:      [0.7051,0.715,0.727,0.728,0.728,0.732,0.736,0.713,0.709,0.722],
  Portugal:    [0.7243,0.731,0.737,0.734,0.732,0.738,0.744,0.775,0.766,0.765],
  Romania:     [0.6936,0.693,0.690,0.708,0.711,0.7175,0.724,0.700,0.698,0.697],
  Slovakia:    [0.6806,0.675,0.679,0.694,0.693,0.7055,0.718,0.712,0.717,0.720],
  Slovenia:    [0.784,0.784,0.786,0.805,0.784,0.780,0.760,0.750,0.760,0.770],
  Spain:       [0.7325,0.742,0.738,0.746,0.795,0.795,0.788,0.788,0.791,0.731],
  Sweden:      [0.8165,0.823,0.815,0.816,0.822,0.820,0.820,0.823,0.822,0.815]
};

// Female prisoners per 100k (averaged from CSV PerHundred for Females)
const FEM_PER_100K = {
  Austria: 6.32, Belgium: 4.21, Bulgaria: 3.32, Croatia: 4.59, Cyprus: 3.36, Czechia: 14.77,
  Denmark: 2.85, Estonia: 9.49, Finland: 4.10, France: 3.40, Germany: 4.23, Greece: 4.93,
  Hungary: 13.63, Ireland: 4.74, Italy: 4.15, Latvia: 15.10, Lithuania: 9.84, Luxembourg: 5.48,
  Malta: 10.51, Netherlands: 3.39, Poland: 8.25, Portugal: 6.85, Romania: 5.91, Slovakia: 13.06,
  Slovenia: 4.50, Spain: 8.20, Sweden: 4.30
};

// Female % of prison population (approx)
const FEM_PCT = {
  Austria: 6.5, Belgium: 4.4, Bulgaria: 3.6, Croatia: 5.0, Cyprus: 6.5, Czechia: 8.4,
  Denmark: 4.5, Estonia: 5.4, Finland: 7.7, France: 3.4, Germany: 5.7, Greece: 5.0,
  Hungary: 7.5, Ireland: 5.0, Italy: 4.3, Latvia: 8.4, Lithuania: 4.4, Luxembourg: 6.0,
  Malta: 8.5, Netherlands: 5.0, Poland: 4.5, Portugal: 7.0, Romania: 4.8, Slovakia: 7.5,
  Slovenia: 7.5, Spain: 7.4, Sweden: 6.0
};

// Country ISO/coords (lat, lon) for the globe pins
const COUNTRY_COORDS = {
  Austria:[47.5,14.5], Belgium:[50.5,4.5], Bulgaria:[42.7,25.5], Croatia:[45.1,15.2],
  Cyprus:[35.1,33.4], Czechia:[49.8,15.5], Denmark:[56.0,10.0], Estonia:[58.6,25.0],
  Finland:[64.0,26.0], France:[46.6,2.5], Germany:[51.2,10.5], Greece:[39.0,22.0],
  Hungary:[47.2,19.5], Ireland:[53.4,-8.0], Italy:[42.8,12.8], Latvia:[56.9,24.6],
  Lithuania:[55.2,24.0], Luxembourg:[49.8,6.1], Malta:[35.9,14.4], Netherlands:[52.2,5.3],
  Poland:[51.9,19.1], Portugal:[39.4,-8.2], Romania:[45.9,24.9], Slovakia:[48.7,19.7],
  Slovenia:[46.1,14.8], Spain:[40.4,-3.7], Sweden:[60.1,18.6]
};

// Regional means per year (computed from GGI table)
function regionalMean(region, year) {
  const yi = YEARS.indexOf(year);
  const ctrs = REGIONS[region];
  const vals = ctrs.map(c => GGI[c][yi]).filter(v => v != null);
  return vals.reduce((a,b)=>a+b,0)/vals.length;
}
function euMean(year) {
  const yi = YEARS.indexOf(year);
  const allCtrs = Object.keys(GGI);
  const vals = allCtrs.map(c => GGI[c][yi]);
  return vals.reduce((a,b)=>a+b,0)/vals.length;
}

const REGIONAL_SERIES = {};
Object.keys(REGIONS).forEach(r => {
  REGIONAL_SERIES[r] = YEARS.map(y => regionalMean(r, y));
});
const EU_SERIES = YEARS.map(y => euMean(y));

window.VIZ_DATA = {
  REGIONS, REGION_COLORS, COUNTRY_REGION, COUNTRY_AVG_GGI, EU_AVG, YEARS,
  GGI, FEM_PER_100K, FEM_PCT, COUNTRY_COORDS, REGIONAL_SERIES, EU_SERIES
};
