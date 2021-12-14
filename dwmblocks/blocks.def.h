//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"", "dwm-brightness", 60, 7},
	{"", "dwm-volume", 0, 6 }, 
	{" ", "dwm-cpu", 2, 5},
	{"﬙ ", "free -m | awk '/^Mem:/ {print $3\" MiB\"}'", 2, 4},
	{" ", "upower -i /org/freedesktop/UPower/devices/battery_BAT0 | awk '/percentage/ {print $2}'", 60, 	3},
	{" ", "date +%d-%m-%Y", 60, 	2},
	{" ", "date +%H:%M", 	60,		1},
	
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = "  ";
static unsigned int delimLen = 5;
