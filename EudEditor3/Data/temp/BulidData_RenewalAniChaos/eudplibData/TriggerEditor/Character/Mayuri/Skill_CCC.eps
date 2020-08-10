import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.HoldPosition(cp);
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);
   MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Ghost", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {                      
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
            f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {
            f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            if (f.loop[cp] % 2 == 0)
            {
               f.SquareShape(cp, 1, "40 + 1n Marine", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);
            }

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;

         }
         else if (f.loop[cp] < 16)
         {                        
            f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12));
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 16)
         {                        
            f.SkillWait(cp, 1080);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 17)
         {                        
            f.Voice_Routine(cp, 6);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {                        
            f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0);
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {
            f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            if (f.loop[cp] % 2 == 1)
            {
               f.SquareShape(cp, 1, "40 + 1n Ghost", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
            }

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;

         }
         else if (f.loop[cp] < 16)
         {                        
            f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12));
            KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 16)
         {                        
            f.SkillWait(cp, 1080);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 17)
         {                        
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (Bring(cp, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill") 
         && f.step[cp] == 210)
         {
            f.Voice_Routine(cp, 7);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 220;
            KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", cp);
         }
         else 
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
            
            SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

            f.SkillEnd(cp);
         }



      }
   }
   if (f.delayB[cp] == 0)
   {
      if ((f.count[cp] == 1) && (f.loop[cp] < 16))
      {
         if (f.loopB[cp] > 3) f.loopB[cp] = 0;

         f.Table_Sin(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50);
         f.Table_Cos(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50); 

         f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         f.SkillWaitB(cp, 160);

         f.loopB[cp] += 1;
      }
   }
   if (f.delayC[cp] == 0)
   {
      if ((f.count[cp] < 2) && (f.loop[cp] < 16))
      {
         if (f.loopC[cp] > 8) f.loopC[cp] = 0;

         f.SquareShape(cp, 1, "40 + 1n Zealot", 240 - 30 * f.loopC[cp], 30 * f.loopC[cp]);
         f.SquareShape(cp, 1, "Protoss Dark Templar", 160 - 20 * f.loopC[cp], 20 * f.loopC[cp]);

         KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
         KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

         f.SkillWaitC(cp, 80);

         f.loopC[cp] += 1;
      }
   }

}