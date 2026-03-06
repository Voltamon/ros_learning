#include <stdio.h>
#include <unistd.h>

#include <rcl/error_handling.h>
#include <rcl/rcl.h>
#include <std_msgs/msg/string.h>

int error_handler(rcl_ret_t code, const char *msg) {
  if (code == RCL_RET_OK)
    return 0;

  if (rcl_error_is_set()) {
    fprintf(stderr, "%s", rcl_get_error_state()->message);
    rcl_reset_error();
  }

  fprintf(stderr, "%s", msg);
  return 1;
}

int rcl_cleanup(rcl_context_t *ctx, rcl_init_options_t *init_ops) {
  rcl_ret_t ret;
  uint8_t error = 0;
  
  if (rcl_context_is_valid(ctx)) {
    ret = rcl_shutdown(ctx);
    if (error_handler(ret, "RCL shutdown failed"))
      error = 1;
  }

  ret = rcl_init_options_fini(init_ops);
  if (error_handler(ret, "Init_Options cleanup failed"))
    error = 1;

  ret = rcl_context_fini(ctx);
  if (error_handler(ret, "Context cleanup failed"))
    error = 1;

  return error;
}

int main(int argc, const char *const *argv) {
  rcl_ret_t ret;

  rcl_allocator_t alloc = rcl_get_default_allocator();
  rcl_context_t ctx = rcl_get_zero_initialized_context();
  rcl_init_options_t init_ops = rcl_get_zero_initialized_init_options();

  ret = rcl_init_options_init(&init_ops, alloc);
  if (error_handler(ret, "Init_Options initialization failed"))
    return 1;

  ret = rcl_init(argc, argv, &init_ops, &ctx);
  if (error_handler(ret, "RCL initialization failed"))
    return 1; 

  rcl_node_t node = rcl_get_zero_initialized_node();
  rcl_node_options_t node_ops = rcl_node_get_default_options();

  ret = rcl_node_init(&node, "basic_rcl_node", "", &ctx, &node_ops);
  if (error_handler(ret, "Node initialization failed"))
    return 1;

  while (rcl_context_is_valid(&ctx))
    sleep(1);

  ret = rcl_node_fini(&node);
  if (error_handler(ret, "Node cleanup failed"))
    return 1;

  return rcl_cleanup(&ctx, &init_ops);
}
