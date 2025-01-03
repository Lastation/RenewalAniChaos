import Function as f;

//0 -> X
//1 -> 활성
//2 -> 대기
var flag = 0;
var pre_flag = 0;

function main(cp)
{
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] < 9)
      {
         if (f.loop[cp] % 20 == 0)
         {
            flag = 2;
         }
         if (f.loop[cp] % 20 == 1)
         {
            f.DotShape(cp, 8, "Zerg Devourer", 0, 0);
            if (cp < 3)
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P7);
            else if (cp >= 3)
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P8);
         }
      }

      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("JunkYardDog - Ekidona", Set);
            f.ShieldFix(cp, 1);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 91)
         {
            f.Voice_Routine(cp, 3);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 66)
         {
            f.Voice_Routine(cp, 4);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 68)
         {
            f.Voice_Routine(cp, 5);

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P7);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P8);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P11);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P9);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P12);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P10);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 57)
         {
            f.Voice_Routine(cp, 6);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 68)
         {
            f.Voice_Routine(cp, 7);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 20)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 6)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.Voice_Routine(cp, 8);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 7)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 15)
         {
            f.Voice_Routine(cp, 9);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 8)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 43)
         {
            f.Voice_Routine(cp, 10);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 9)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 18)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 10)
      {
         if (Bring(cp, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill") 
         && Deaths(cp, AtLeast, f.UltimateB[cp], " `UltimateCoolTime"))
         {
            f.Voice_Routine(cp, 11);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 320;
            SetDeaths(cp, Subtract, f.UltimateB[cp], " `UltimateCoolTime");
            KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         else
         {
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P7);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P8);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P11);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P9);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P12);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", P10);

            SetSwitch("JunkYardDog - Ekidona", Clear);
            SetSwitch("UiltimateSwitch", Clear);
            f.SkillEnd(cp);
         }
      }

      if (cp < 3)
      {
         if (Bring(P7, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 8; i++)
            {
               MoveLocation(f.location[cp], "Zerg Devourer", P7, "Anywhere");
               GiveUnits(1, "Zerg Devourer", P7, "Anywhere", P9);

               if (i % 2 == 0) 
               {
                  f.SkillUnit(cp, 1, "80 + 1n Tom Kazansky");
                  f.SkillUnit(cp, 1, "Protoss Dark Archon");
               }
               else if (i % 2 == 1)
               {
                  f.SkillUnit(cp, 1, "80 + 1n Artanis");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
            }

            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else
         {
            GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P7);
         }
      }
      else if (cp >= 3)
      {
         if (Bring(P8, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 8; i++)
            {
               MoveLocation(f.location[cp], "Zerg Devourer", P8, "Anywhere");
               GiveUnits(1, "Zerg Devourer", P8, "Anywhere", P9);

               if (i % 2 == 0) 
               {
                  f.SkillUnit(cp, 1, "80 + 1n Tom Kazansky");
                  f.SkillUnit(cp, 1, "Protoss Dark Archon");
               }
               else if (i % 2 == 1)
               {
                  f.SkillUnit(cp, 1, "80 + 1n Artanis");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
            }

            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else
         {
            GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P8);
         }
      }

      if (flag == 1)
      {
         if (pre_flag != flag)
         {
            GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10);
            GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P10);

            pre_flag = flag;
         }
         if (Bring(P10, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 8; i++)
            {
               MoveLocation(f.location[cp], "Zerg Devourer", P10, "Anywhere");
               GiveUnits(1, "Zerg Devourer", P10, "Anywhere", P11);

               if (i % 2 == 0) 
               {
                  f.SkillUnit(cp, 1, "80 + 1n Tom Kazansky");
                  f.SkillUnit(cp, 1, "Protoss Dark Archon");
               }
               else if (i % 2 == 1)
               {
                  f.SkillUnit(cp, 1, "80 + 1n Artanis");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
            }

            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else
         {
            GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10);
         }
      }
      else if (flag == 2)
      {
         if (pre_flag != flag)
         {
            GiveUnits(All, "Zerg Devourer", P9, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P7, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P8, "Anywhere", cp);

            MoveUnit(All, "Zerg Devourer", cp, "Anywhere", "[Skill]HoldPosition");

            pre_flag = flag;
         }

         if (Bring(cp, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 8; i++)
            {
               MoveLocation(f.location[cp], "Zerg Devourer", cp, "Anywhere");
               GiveUnits(1, "Zerg Devourer", cp, "Anywhere", P11);

               if (i % 4 == 0) 
               {
                  f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                  f.SkillUnit(cp, 1, "60 + 1n Siege");
                  f.SkillUnit(cp, 1, "130 + 1n Norad");
               }
               else if (i % 4 == 1)
               {
                  f.SkillUnit(cp, 1, "60 + 1n Danimoth");
                  f.SkillUnit(cp, 1, "60 + 1n Siege");
                  f.SkillUnit(cp, 1, "40 + 1n Gantrithor");
               }
               else if (i % 4 == 2)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Wraith");
                  f.SkillUnit(cp, 1, "50 + 1n Tank");
                  f.SkillUnit(cp, 1, "130 + 1n Norad");
               }
               else if (i % 4 == 3)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Mojo");
                  f.SkillUnit(cp, 1, "60 + 1n Dragoon");
                  f.SkillUnit(cp, 1, "40 + 1n Gantrithor");
               }
            }

            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         else
         {
            flag = 1;
         }
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}