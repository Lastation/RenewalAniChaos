import Function as f;

const s = StringBuffer();

function main(cp)
{
   MoveUnit(All, "50 + 1n Battlecruiser", cp, "Anywhere", "[Skill]HoldPosition");
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.count[cp] < 2)
   {
      SetAllianceStatus(P7, Ally);
      SetAllianceStatus(P8, Ally);
   }

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 12)
         {    
            SetSwitch("ComputerAlliy", Set);

            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.Table_Sin(cp, (30 * f.loop[cp]), 160);
            f.Table_Cos(cp, (30 * f.loop[cp]), 160); 

            f.SquareShape(cp, 1, "60 + 3n Siege", 120 + f.CosAngle[cp], 120 + f.SinAngle[cp]);
            f.SquareShape(cp, 16, "80 + 1n Vulture", 120 + f.CosAngle[cp], 120 + f.SinAngle[cp]);
            GiveUnits(All, "60 + 3n Siege", cp, "Anywhere", P9);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Vulture", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {       
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.SkillWait(cp, 640);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 12)
         {    
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.Table_Sin(cp, (30 * f.loop[cp]), 160);
            f.Table_Cos(cp, (30 * f.loop[cp]), 160); 

            f.SquareShape(cp, 1, "60 + 3n Siege", 160 + f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 16, "80 + 1n Vulture", 160 + f.CosAngle[cp], f.SinAngle[cp]);
            GiveUnits(All, "60 + 3n Siege", cp, "Anywhere", P9);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Vulture", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {       
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.SkillWait(cp, 560);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 13)
         {       
            f.Voice_Routine(cp, 11);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 12)
         {    
            SetSwitch("ComputerAlliy", Clear);

            if (cp < 3)
            {
               SetAllianceStatus(P8, Enemy);
            }
            else
            {
               SetAllianceStatus(P7, Enemy);
            }

            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.Table_Sin(cp, (30 * f.loop[cp]), 160);
            f.Table_Cos(cp, (30 * f.loop[cp]), 160); 

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 120 + f.CosAngle[cp], 120 + f.SinAngle[cp]);
            f.SquareShape(cp, 8, "80 + 1n Vulture", 120 + f.CosAngle[cp], 120 + f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Vulture", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {       
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.SkillWait(cp, 1760);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 13)
         {       
            f.Voice_Routine(cp, 12);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 12)
         {    
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.Table_Sin(cp, (30 * f.loop[cp]), 160);
            f.Table_Cos(cp, (30 * f.loop[cp]), 160); 

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 160 + f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 8, "80 + 1n Vulture", 160 + f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "80 + 1n Vulture", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Vulture", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {       
            KillUnitAt(All, "80 + 1n Vulture", "Anywhere", cp);

            f.SkillWait(cp, 560);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 13)
         {       
            f.SkillWait(cp, 1440);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 4)
      {
         if (Bring(cp, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
         && Deaths(cp, AtLeast, f.UltimateB[cp], " `UltimateCoolTime"))
         {
            if (Switch("UiltimateSwitch", Cleared))
            {
               SetSwitch("UiltimateSwitch", Set);
               CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
               f.Voice_Routine(cp, 13);
               f.wait[cp] = 0;
               f.count[cp] = 0;
               f.loop[cp] = 0;
               f.step[cp] = 330;
               SetDeaths(cp, Subtract, f.UltimateB[cp], " `UltimateCoolTime");
               KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
            }
            else
            {
               SetResources(CurrentPlayer, Add, 600, Gas);
               KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
               SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
               KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
               KillUnitAt(All, "60 + 3n Siege", "Anywhere", P9);
               SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
               f.SkillEnd(cp);
            }
         }
         else 
         {
            SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 3n Siege", "Anywhere", P9);
            f.SkillEnd(cp);
         }



      }
   }
}