#define MODULE
#define LINUX


#include linuxmodule.h   
#include linuxkernel.h   


int init_module(void)
{
   printk(1Hello world 1.n);
	
   return 0;
}


void cleanup_module(void)
{
  printk(KERN_ALERT Goodbye world 1.n);
}  

MODULE_LICENSE(GPL);
