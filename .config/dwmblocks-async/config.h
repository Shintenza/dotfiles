#define CMDLENGTH 100
#define DELIMITER "  "
#define CLICKABLE_BLOCKS

const Block blocks[] = {
	BLOCK("sb-volume",          10,         6),
	BLOCK("sb-battery",         10,         5),
	BLOCK("sb-brightness",      10,         4),
	BLOCK("sb-cpu",              2,         3),
	BLOCK("sb-memory",           2,         2),
	BLOCK("sb-network",         10,         1),
	BLOCK("sb-clock",            1,         0)
};
