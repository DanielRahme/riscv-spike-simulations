
#include <fft_input_array.h>


float input_f32_fft_64[128] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_128[256] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_256[512] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_512[1024] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_1024[2048] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_2048[4096] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_4096[8192] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

float input_f32_fft_8192[16384] = {
    -46.253014579396876f,
    -78.73988485657893f,
    49.3653691064973f,
    32.754407839495656f,
    -45.519782835119685f,
    72.45625033826974f,
    78.31445243386466f,
    69.96295708388968f,
    73.44952523426176f,
    94.32797813318288f,
    -9.762544171649125f,
    71.45996727669322f,
    78.44171197345574f,
    -98.03209620899884f,
    31.528808330190145f,
    -7.248141762264098f,
    27.298067427564575f,
    -72.81701820859585f,
    41.634546352461655f,
    76.15459009962433f,
    33.40506237725714f,
    -36.073468563414266f,
    79.37736580280426f,
    -74.7393629412212f,
    22.423825616914115f,
    -1.9036070939304466f,
    -70.25350701011692f,
    -72.83506730456503f,
    -14.571995766672856f,
    55.125505682952735f,
    62.40541415496236f,
    60.759538372190974f,
    90.65606705443994f,
    78.11320378472843f,
    58.31289856086684f,
    -98.70768655046052f,
    -56.99968403092692f,
    -36.738802526871716f,
    0.5940771383257157f,
    9.237988451645123f,
    -74.56883120155581f,
    -74.63802888217022f,
    52.685215820847674f,
    -29.264399717726675f,
    -21.41643940008339f,
    17.941769796363488f,
    -63.74534327757808f,
    8.195525179775558f,
    -73.22847422182343f,
    -44.731488728475895f,
    -27.19860985495619f,
    -57.23352915762439f,
    -98.82466409558626f,
    33.433246746936675f,
    1.0041791656316406f,
    30.52202838105387f,
    -90.47276568723316f,
    4.61310337903285f,
    -33.07231192882141f,
    -3.3517850331954406f,
    -49.30233793199652f,
    50.29998868351353f,
    19.555908620379014f,
    43.0650815711756f,
    -59.10587441499062f,
    -80.03356293092307f,
    -5.515823785190491f,
    33.7576164642027f,
    93.52056666126379f,
    47.22261022729376f,
    92.47132201020969f,
    43.32249104264872f,
    -10.536177087326664f,
    6.346662292085512f,
    -47.36967705040635f,
    -83.31551607162811f,
    79.6641777127966f,
    48.20334160940271f,
    36.10808859601525f,
    79.3515481227123f,
    -53.119150472229215f,
    -18.792700588621685f,
    -12.062293417035065f,
    -79.99601345979067f,
    82.28092428718696f,
    -57.73199098198067f,
    36.28057300259482f,
    -45.56659753621077f,
    48.71506100901283f,
    68.75351373742794f,
    51.03539917942484f,
    -99.49827833974238f,
    -82.95185357436483f,
    -39.7563150350632f,
    -50.02215707840798f,
    38.66888207111563f,
    -42.38340455579157f,
    51.47316461673876f,
    35.047909139854085f,
    68.18379708472415f,
    86.34301309439775f,
    -33.308865076152784f,
    30.560041753350646f,
    31.0991438356225f,
    39.43132466082119f,
    -70.15130802934273f,
    95.48519167628226f,
    97.61358696335842f,
    -33.46718366024548f,
    39.72028119259136f,
    47.06245182800524f,
    78.55920662288068f,
    4.957508349094738f,
    86.37730921545614f,
    -95.50619779399676f,
    -58.495161050467814f,
    63.286282843678805f,
    55.914987624234044f,
    -83.90789817091056f,
    -65.9374463823073f,
    63.5967112677358f,
    -96.96857849734928f,
    -89.86970758455064f,
    63.883691334234896f,
    -26.54858835407947f,
    -21.969119210717608f,
    80.66033615891862f,
    35.615364892579805f,
};

