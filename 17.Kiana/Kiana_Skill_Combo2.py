
Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
	  Wait(300);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 112, 48);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -112, 48);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -48, 144);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 48, 144);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, 16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, 16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, -16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, -16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -48, -16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 48, -16);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, -48);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, -48);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -128, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -128, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -96, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -96, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 128, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 128, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 96, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 96, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -64, 160);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, 160);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -64, 128);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, 128);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 64, 160);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, 160);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 64, 128);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, 128);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(6, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -64, 0);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -64, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, 0);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -32, -64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(6, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 64, 0);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 64, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, 0);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 32, -64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
      Deaths(CurrentPlayer, AtMost, 5, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, -64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
	  Wait(0);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
      Deaths(CurrentPlayer, AtLeast, 6, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(5, "Zerg Devourer", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, 64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, 32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, -32);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 0, -64);
      MoveUnit(1, "Zerg Devourer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Zerg Devourer", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
	  Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 112, 48);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -112, 48);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -48, 144);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 48, 144);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, 16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, 16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, -16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, -16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Fenix");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Fenix", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -48, -16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 48, -16);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, -16, -48);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      LMove(169, 16, -48);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "17.Kiana");
      MoveLocation("17.Kiana", " * Fenix", CurrentPlayer, "Anywhere");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "17.Kiana");
	  Wait(130);
      RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      Wait(1000);
      SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
   },
}
