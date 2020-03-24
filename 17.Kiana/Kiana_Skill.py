
Trigger { -- 16.Seraphim
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4001, " * Fenix");
	},
	actions = {
		Comment("17.Kiana");
		SetDeaths(CurrentPlayer, SetTo, 1000, " `DeadCount");
		SetDeaths(AllPlayers, SetTo, 16, " `DeadText");
		SetDeaths(CurrentPlayer, SetTo, 4000, " * Fenix");
		CreateUnit(1, " * Fenix", "[Select]Select Unit", CurrentPlayer);
		SetInvincibility(Enable, "Men", CurrentPlayer, "[Select]Select Unit");
		PreserveTrigger();
	},
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Use Unique
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill");
		Score(CurrentPlayer, Custom, AtMost, 24);
	},
	actions = {
		Comment("Skill : Use Unique");
		KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", CurrentPlayer);
		SetResources(CurrentPlayer, Add, 60, Gas);
		PreserveTrigger();
		DisplayText("\x13\x17[ O Skill \x04은 25레벨 이상시에만 사용이 가능합니다. \x17]", 0);
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 100, " `SkillStep");
		KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 200, " `SkillStep");
		KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Skill
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
		Bring(CurrentPlayer, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Skill");
		SetDeaths(CurrentPlayer, SetTo, 300, " `SkillStep");
		KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- Skill : Use Combo
	players = {Force1, Force2},
	conditions = {
		Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
		Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
		Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
		Deaths(CurrentPlayer, AtLeast, 2, " `SkillWait");
		Bring(CurrentPlayer, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill");
	},
	actions = {
		Comment("Skill : Use Combo");
		SetDeaths(AllPlayers, SetTo, 5000, " `SkillText3");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillWait");
		SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
		SetDeaths(CurrentPlayer, SetTo, 110, " `SkillStep");
		KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", CurrentPlayer);
		PreserveTrigger();
	},
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

x = 96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(130);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(130);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(130);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(130);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
	  Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x = 96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x = -32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(130);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
	  Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
   },
}