# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ALLOCATION_SITE_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "CONTEXT_EXTENSION_TYPE",
  161: "DEBUG_INFO_TYPE",
  162: "FUNCTION_TEMPLATE_INFO_TYPE",
  163: "INTERCEPTOR_INFO_TYPE",
  164: "INTERPRETER_DATA_TYPE",
  165: "MODULE_INFO_ENTRY_TYPE",
  166: "MODULE_TYPE",
  167: "OBJECT_TEMPLATE_INFO_TYPE",
  168: "PROMISE_CAPABILITY_TYPE",
  169: "PROMISE_REACTION_TYPE",
  170: "PROTOTYPE_INFO_TYPE",
  171: "SCRIPT_TYPE",
  172: "STACK_FRAME_INFO_TYPE",
  173: "TUPLE2_TYPE",
  174: "TUPLE3_TYPE",
  175: "WASM_COMPILED_MODULE_TYPE",
  176: "WASM_DEBUG_INFO_TYPE",
  177: "WASM_SHARED_MODULE_DATA_TYPE",
  178: "CALLABLE_TASK_TYPE",
  179: "CALLBACK_TASK_TYPE",
  180: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  181: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  182: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  183: "FIXED_ARRAY_TYPE",
  184: "BOILERPLATE_DESCRIPTION_TYPE",
  185: "DESCRIPTOR_ARRAY_TYPE",
  186: "HASH_TABLE_TYPE",
  187: "SCOPE_INFO_TYPE",
  188: "BLOCK_CONTEXT_TYPE",
  189: "CATCH_CONTEXT_TYPE",
  190: "DEBUG_EVALUATE_CONTEXT_TYPE",
  191: "EVAL_CONTEXT_TYPE",
  192: "FUNCTION_CONTEXT_TYPE",
  193: "MODULE_CONTEXT_TYPE",
  194: "NATIVE_CONTEXT_TYPE",
  195: "SCRIPT_CONTEXT_TYPE",
  196: "WITH_CONTEXT_TYPE",
  197: "WEAK_FIXED_ARRAY_TYPE",
  198: "TRANSITION_ARRAY_TYPE",
  199: "CALL_HANDLER_INFO_TYPE",
  200: "CELL_TYPE",
  201: "CODE_DATA_CONTAINER_TYPE",
  202: "FEEDBACK_CELL_TYPE",
  203: "FEEDBACK_VECTOR_TYPE",
  204: "LOAD_HANDLER_TYPE",
  205: "PROPERTY_ARRAY_TYPE",
  206: "PROPERTY_CELL_TYPE",
  207: "SHARED_FUNCTION_INFO_TYPE",
  208: "SMALL_ORDERED_HASH_MAP_TYPE",
  209: "SMALL_ORDERED_HASH_SET_TYPE",
  210: "STORE_HANDLER_TYPE",
  211: "WEAK_CELL_TYPE",
  212: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1076: "JS_SET_TYPE",
  1077: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1078: "JS_SET_VALUE_ITERATOR_TYPE",
  1079: "JS_STRING_ITERATOR_TYPE",
  1080: "JS_WEAK_MAP_TYPE",
  1081: "JS_WEAK_SET_TYPE",
  1082: "JS_TYPED_ARRAY_TYPE",
  1083: "JS_DATA_VIEW_TYPE",
  1084: "WASM_GLOBAL_TYPE",
  1085: "WASM_INSTANCE_TYPE",
  1086: "WASM_MEMORY_TYPE",
  1087: "WASM_MODULE_TYPE",
  1088: "WASM_TABLE_TYPE",
  1089: "JS_BOUND_FUNCTION_TYPE",
  1090: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x02201): (132, "MetaMap"),
  ("RO_SPACE", 0x02289): (131, "NullMap"),
  ("RO_SPACE", 0x02301): (185, "DescriptorArrayMap"),
  ("RO_SPACE", 0x02369): (183, "FixedArrayMap"),
  ("RO_SPACE", 0x023d1): (211, "WeakCellMap"),
  ("RO_SPACE", 0x024e9): (131, "UndefinedMap"),
  ("RO_SPACE", 0x02591): (131, "TheHoleMap"),
  ("RO_SPACE", 0x02701): (183, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x02839): (197, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x028a1): (212, "WeakArrayListMap"),
  ("RO_SPACE", 0x02921): (173, "Tuple2Map"),
  ("RO_SPACE", 0x02999): (171, "ScriptMap"),
  ("RO_SPACE", 0x02a01): (163, "InterceptorInfoMap"),
  ("RO_SPACE", 0x06891): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x06aa1): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x06b09): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x06b71): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x06bd9): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x06c41): (158, "AllocationSiteMap"),
  ("RO_SPACE", 0x06ca9): (159, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x06d11): (160, "ContextExtensionMap"),
  ("RO_SPACE", 0x06d79): (161, "DebugInfoMap"),
  ("RO_SPACE", 0x06de1): (162, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x06e49): (164, "InterpreterDataMap"),
  ("RO_SPACE", 0x06eb1): (165, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x06f19): (166, "ModuleMap"),
  ("RO_SPACE", 0x06f81): (167, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x06fe9): (168, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x07051): (169, "PromiseReactionMap"),
  ("RO_SPACE", 0x070b9): (170, "PrototypeInfoMap"),
  ("RO_SPACE", 0x07121): (172, "StackFrameInfoMap"),
  ("RO_SPACE", 0x07189): (174, "Tuple3Map"),
  ("RO_SPACE", 0x071f1): (175, "WasmCompiledModuleMap"),
  ("RO_SPACE", 0x07259): (176, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x072c1): (177, "WasmSharedModuleDataMap"),
  ("RO_SPACE", 0x07329): (178, "CallableTaskMap"),
  ("RO_SPACE", 0x07391): (179, "CallbackTaskMap"),
  ("RO_SPACE", 0x073f9): (180, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x07461): (181, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x074c9): (182, "PromiseResolveThenableJobTaskMap"),
  ("MAP_SPACE", 0x02201): (138, "FreeSpaceMap"),
  ("MAP_SPACE", 0x02259): (152, "OnePointerFillerMap"),
  ("MAP_SPACE", 0x022b1): (152, "TwoPointerFillerMap"),
  ("MAP_SPACE", 0x02309): (131, "UninitializedMap"),
  ("MAP_SPACE", 0x02361): (8, "OneByteInternalizedStringMap"),
  ("MAP_SPACE", 0x023b9): (129, "HeapNumberMap"),
  ("MAP_SPACE", 0x02411): (131, "BooleanMap"),
  ("MAP_SPACE", 0x02469): (136, "ByteArrayMap"),
  ("MAP_SPACE", 0x024c1): (186, "HashTableMap"),
  ("MAP_SPACE", 0x02519): (128, "SymbolMap"),
  ("MAP_SPACE", 0x02571): (72, "OneByteStringMap"),
  ("MAP_SPACE", 0x025c9): (187, "ScopeInfoMap"),
  ("MAP_SPACE", 0x02621): (207, "SharedFunctionInfoMap"),
  ("MAP_SPACE", 0x02679): (133, "CodeMap"),
  ("MAP_SPACE", 0x026d1): (192, "FunctionContextMap"),
  ("MAP_SPACE", 0x02729): (200, "CellMap"),
  ("MAP_SPACE", 0x02781): (206, "GlobalPropertyCellMap"),
  ("MAP_SPACE", 0x027d9): (135, "ForeignMap"),
  ("MAP_SPACE", 0x02831): (198, "TransitionArrayMap"),
  ("MAP_SPACE", 0x02889): (203, "FeedbackVectorMap"),
  ("MAP_SPACE", 0x028e1): (131, "ArgumentsMarkerMap"),
  ("MAP_SPACE", 0x02939): (131, "ExceptionMap"),
  ("MAP_SPACE", 0x02991): (131, "TerminationExceptionMap"),
  ("MAP_SPACE", 0x029e9): (131, "OptimizedOutMap"),
  ("MAP_SPACE", 0x02a41): (131, "StaleRegisterMap"),
  ("MAP_SPACE", 0x02a99): (194, "NativeContextMap"),
  ("MAP_SPACE", 0x02af1): (193, "ModuleContextMap"),
  ("MAP_SPACE", 0x02b49): (191, "EvalContextMap"),
  ("MAP_SPACE", 0x02ba1): (195, "ScriptContextMap"),
  ("MAP_SPACE", 0x02bf9): (188, "BlockContextMap"),
  ("MAP_SPACE", 0x02c51): (189, "CatchContextMap"),
  ("MAP_SPACE", 0x02ca9): (196, "WithContextMap"),
  ("MAP_SPACE", 0x02d01): (190, "DebugEvaluateContextMap"),
  ("MAP_SPACE", 0x02d59): (183, "ScriptContextTableMap"),
  ("MAP_SPACE", 0x02db1): (151, "FeedbackMetadataArrayMap"),
  ("MAP_SPACE", 0x02e09): (183, "ArrayListMap"),
  ("MAP_SPACE", 0x02e61): (130, "BigIntMap"),
  ("MAP_SPACE", 0x02eb9): (184, "BoilerplateDescriptionMap"),
  ("MAP_SPACE", 0x02f11): (137, "BytecodeArrayMap"),
  ("MAP_SPACE", 0x02f69): (201, "CodeDataContainerMap"),
  ("MAP_SPACE", 0x02fc1): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x03019): (150, "FixedDoubleArrayMap"),
  ("MAP_SPACE", 0x03071): (186, "GlobalDictionaryMap"),
  ("MAP_SPACE", 0x030c9): (202, "ManyClosuresCellMap"),
  ("MAP_SPACE", 0x03121): (1072, "JSMessageObjectMap"),
  ("MAP_SPACE", 0x03179): (183, "ModuleInfoMap"),
  ("MAP_SPACE", 0x031d1): (134, "MutableHeapNumberMap"),
  ("MAP_SPACE", 0x03229): (186, "NameDictionaryMap"),
  ("MAP_SPACE", 0x03281): (202, "NoClosuresCellMap"),
  ("MAP_SPACE", 0x032d9): (186, "NumberDictionaryMap"),
  ("MAP_SPACE", 0x03331): (202, "OneClosureCellMap"),
  ("MAP_SPACE", 0x03389): (186, "OrderedHashMapMap"),
  ("MAP_SPACE", 0x033e1): (186, "OrderedHashSetMap"),
  ("MAP_SPACE", 0x03439): (205, "PropertyArrayMap"),
  ("MAP_SPACE", 0x03491): (199, "SideEffectCallHandlerInfoMap"),
  ("MAP_SPACE", 0x034e9): (199, "SideEffectFreeCallHandlerInfoMap"),
  ("MAP_SPACE", 0x03541): (186, "SimpleNumberDictionaryMap"),
  ("MAP_SPACE", 0x03599): (183, "SloppyArgumentsElementsMap"),
  ("MAP_SPACE", 0x035f1): (208, "SmallOrderedHashMapMap"),
  ("MAP_SPACE", 0x03649): (209, "SmallOrderedHashSetMap"),
  ("MAP_SPACE", 0x036a1): (186, "StringTableMap"),
  ("MAP_SPACE", 0x036f9): (106, "NativeSourceStringMap"),
  ("MAP_SPACE", 0x03751): (64, "StringMap"),
  ("MAP_SPACE", 0x037a9): (73, "ConsOneByteStringMap"),
  ("MAP_SPACE", 0x03801): (65, "ConsStringMap"),
  ("MAP_SPACE", 0x03859): (77, "ThinOneByteStringMap"),
  ("MAP_SPACE", 0x038b1): (69, "ThinStringMap"),
  ("MAP_SPACE", 0x03909): (67, "SlicedStringMap"),
  ("MAP_SPACE", 0x03961): (75, "SlicedOneByteStringMap"),
  ("MAP_SPACE", 0x039b9): (66, "ExternalStringMap"),
  ("MAP_SPACE", 0x03a11): (82, "ExternalStringWithOneByteDataMap"),
  ("MAP_SPACE", 0x03a69): (74, "ExternalOneByteStringMap"),
  ("MAP_SPACE", 0x03ac1): (98, "ShortExternalStringMap"),
  ("MAP_SPACE", 0x03b19): (114, "ShortExternalStringWithOneByteDataMap"),
  ("MAP_SPACE", 0x03b71): (0, "InternalizedStringMap"),
  ("MAP_SPACE", 0x03bc9): (2, "ExternalInternalizedStringMap"),
  ("MAP_SPACE", 0x03c21): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("MAP_SPACE", 0x03c79): (10, "ExternalOneByteInternalizedStringMap"),
  ("MAP_SPACE", 0x03cd1): (34, "ShortExternalInternalizedStringMap"),
  ("MAP_SPACE", 0x03d29): (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  ("MAP_SPACE", 0x03d81): (42, "ShortExternalOneByteInternalizedStringMap"),
  ("MAP_SPACE", 0x03dd9): (106, "ShortExternalOneByteStringMap"),
  ("MAP_SPACE", 0x03e31): (140, "FixedUint8ArrayMap"),
  ("MAP_SPACE", 0x03e89): (139, "FixedInt8ArrayMap"),
  ("MAP_SPACE", 0x03ee1): (142, "FixedUint16ArrayMap"),
  ("MAP_SPACE", 0x03f39): (141, "FixedInt16ArrayMap"),
  ("MAP_SPACE", 0x03f91): (144, "FixedUint32ArrayMap"),
  ("MAP_SPACE", 0x03fe9): (143, "FixedInt32ArrayMap"),
  ("MAP_SPACE", 0x04041): (145, "FixedFloat32ArrayMap"),
  ("MAP_SPACE", 0x04099): (146, "FixedFloat64ArrayMap"),
  ("MAP_SPACE", 0x040f1): (147, "FixedUint8ClampedArrayMap"),
  ("MAP_SPACE", 0x04149): (149, "FixedBigUint64ArrayMap"),
  ("MAP_SPACE", 0x041a1): (148, "FixedBigInt64ArrayMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x02259): "NullValue",
  ("RO_SPACE", 0x022e1): "EmptyDescriptorArray",
  ("RO_SPACE", 0x02359): "EmptyFixedArray",
  ("RO_SPACE", 0x024b9): "UndefinedValue",
  ("RO_SPACE", 0x02551): "NanValue",
  ("RO_SPACE", 0x02561): "TheHoleValue",
  ("RO_SPACE", 0x02619): "HoleNanValue",
  ("RO_SPACE", 0x02629): "TrueValue",
  ("RO_SPACE", 0x02699): "FalseValue",
  ("RO_SPACE", 0x026e9): "empty_string",
  ("RO_SPACE", 0x02989): "EmptyByteArray",
  ("OLD_SPACE", 0x02201): "UninitializedValue",
  ("OLD_SPACE", 0x02231): "EmptyScopeInfo",
  ("OLD_SPACE", 0x02241): "ArgumentsMarker",
  ("OLD_SPACE", 0x02271): "Exception",
  ("OLD_SPACE", 0x022a1): "TerminationException",
  ("OLD_SPACE", 0x022d1): "OptimizedOut",
  ("OLD_SPACE", 0x02301): "StaleRegister",
  ("OLD_SPACE", 0x02361): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x02381): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x023a1): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x023c1): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x023e1): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x02401): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x02421): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x02441): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x02461): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x024c1): "EmptyScript",
  ("OLD_SPACE", 0x02559): "ManyClosuresCell",
  ("OLD_SPACE", 0x02569): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x02589): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x025d1): "EmptyOrderedHashMap",
  ("OLD_SPACE", 0x025f9): "EmptyOrderedHashSet",
  ("OLD_SPACE", 0x02631): "EmptyPropertyCell",
  ("OLD_SPACE", 0x02659): "EmptyWeakCell",
  ("OLD_SPACE", 0x026e1): "NoElementsProtector",
  ("OLD_SPACE", 0x02709): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x02719): "SpeciesProtector",
  ("OLD_SPACE", 0x02741): "StringLengthProtector",
  ("OLD_SPACE", 0x02751): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02779): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02801): "InfinityValue",
  ("OLD_SPACE", 0x02811): "MinusZeroValue",
  ("OLD_SPACE", 0x02821): "MinusInfinityValue",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
