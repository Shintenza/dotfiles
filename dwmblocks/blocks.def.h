//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"", "dwm-brightness",      60,     7},
	{"", "dwm-volume",          30,     6}, 
	{"", "dwm-cpu",             2,      5},
	{"", "dwm-memory",          2,      4},
	{"", "dwm-battery",         60,     3},
	{"", "dwm-date",            60, 	2},
	{"", "dwm-time", 	        1,		1},
	
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = "  ";
static unsigned int delimLen = 5;
