import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.count[cp] == 1)
   {
      MoveLocation("25.Milim_Bozo", f.heroID[cp], cp, "Anywhere");
   }

   f.HoldPosition(cp);
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            CreateUnit(1, "Flame Blue", "[Skill]Unit_Wait_8", cp);  
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Flame Blue", cp, "Anywhere", f.location[cp]);
            MoveLocation("25.Milim_Bozo", "Flame Blue", cp, "Anywhere");

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 60)
         {      
            var x = 50;

            if (cp >= 3) x = -x;

            f.DotShape(cp, 8, "40 + 1n Zealot", 0, 0);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            addloc("25.Milim_Bozo", x * 3, 0);
            MoveUnit(All, "Flame Blue", cp, "Anywhere", "25.Milim_Bozo");

            CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", cp);  
            SetInvincibility(Enable, "Any unit", cp, "[Skill]Unit_Wait_ALL");

            MoveLocation(f.location[cp], "Flame Blue", cp, "Anywhere");
            MoveUnit(1, "40 + 1n Wraith", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            addloc(f.location[cp], -x, 0);
            MoveUnit(1, "40 + 1n Wraith", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            addloc(f.location[cp], -x, 0);
            MoveUnit(1, "40 + 1n Wraith", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            if ((cp >= 3 && (Bring(cp, AtLeast, 1, "Flame Blue", "[Potal]Shop7") || Bring(cp, AtLeast, 1, "Flame Blue", "[Potal]Potal7")))
               || (cp < 3 && (Bring(cp, AtLeast, 1, "Flame Blue", "[Potal]Shop8") || Bring(cp, AtLeast, 1, "Flame Blue", "[Potal]Potal8"))))
            {
               SetDeaths(cp, SetTo, 120, " `UniqueCoolTime");

               f.SkillWait(cp, 80);

               f.count[cp] = 2;
               f.loop[cp] = 0;
            }
            else if (cp < 3)
            {
               if (Bring(P8, AtLeast, 1, "Buildings", "25.Milim_Bozo"))
               {
                  SetSwitch("Unique - MilimWarning", Set);
                  SetSwitch("Recall - Milim", Set);

                  f.Voice_Routine(cp, 3);

                  f.SkillWait(cp, 80);

                  f.count[cp] += 1;
                  f.loop[cp] = 0;
               }
               else
               {
                  f.SkillWait(cp, 80);

                  f.loop[cp] += 1;
               }
            }
            else if (cp >= 3)
            {
               if (Bring(P7, AtLeast, 1, "Buildings", "25.Milim_Bozo"))
               {
                  SetSwitch("Unique - MilimWarning", Set);
                  SetSwitch("Recall - Milim", Set);

                  f.Voice_Routine(cp, 3); 

                  f.SkillWait(cp, 80);

                  f.count[cp] += 1;
                  f.loop[cp] = 0;
               }
               else
               {
                  f.SkillWait(cp, 80);

                  f.loop[cp] += 1;
               }
            }
         }
         else if (f.loop[cp] == 60)
         {      
            SetDeaths(cp, SetTo, 120, " `UniqueCoolTime");

            f.SkillWait(cp, 80);
            
            f.count[cp] = 2;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 40)
         {      
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 7, 120);
            if (f.loop[cp] % 2 == 0)
            {
               f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3, 40);
            }
            else if (f.loop[cp] % 2 == 1)
            {
               f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 5, 80);
            }
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 40)
         {      
            MoveLocation("25.Milim_Bozo", "Flame Blue", cp, "Anywhere");

            if (Deaths(CurrentPlayer, Exactly, 0, (210)))
            {
               MoveUnit(All, f.heroID[cp], cp, "Anywhere", "25.Milim_Bozo");
               CenterView("25.Milim_Bozo");
            }

            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 3, 75);
            f.DotShape(cp, 16, "80 + 1n Goliath", 0, 0);
            Order("130 + 1n Norad", cp, "Anywhere", Attack, "Anywhere");
            MoveUnit(All, "80 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, "Anywhere");
            SetSwitch("Recall - Milim", Clear);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 45)
         {      
            var i = f.loop[cp] - 41;

            f.EdgeShape(cp, 1, "60 + 1n Siege", 0, 5 + 2 * i, 100 + 50 * i);
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 0, 3 + 2 * i, 50 + 50 * i);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 45)
         {      
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);

            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 3, 50);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 100);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 7, 150);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 9, 150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 46)
         {     
            f.Voice_Routine(cp, 4); 
            SetSwitch("Unique - Milim", Set);
            SetDeaths(cp, SetTo, 2880, " `UniqueCoolTime");
            SetDeaths(cp, SetTo, 720, " `UniqueSkill");

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         RemoveUnitAt(All, "Flame Blue", "Anywhere", cp);
         SetSwitch("Unique - MilimWarning", Clear);
         f.SkillEnd(cp);
      }

   }
}